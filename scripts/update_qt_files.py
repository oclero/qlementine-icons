import os
import re
import pathlib
import sys
from string import Template
from subprocess import call
import json


def this_dir_path():
  return pathlib.Path(__file__).parent.absolute().as_posix()


ICONS_DIR = 'sources/resources/icons'

CPP_FILEPATH = 'sources/src/icons/QlementineIcons.cpp'
CPP_REGEXP_QRC = r'(\/\/ ---QRC.*)\s+((?:.*\n)*)\s+(\/\/ ---QRC)'
CPP_REGEXP_MAP = r'(\/\/ ---MAP.*)\s+((?:.*\n)*)\s+(\/\/ ---MAP)'

HPP_ENUM_DIR = 'sources/include/oclero/qlementine/icons/'
HPP_ENUM_NAME_REGEX = r'(.*\/)(.*\.svg)'
HPP_ENUM_TEMPLATE_FILEPATH = this_dir_path() + '/resources/Template.hpp'

QRC_TEMPLATE_FILEPATH = this_dir_path() + '/resources/Template.qrc'

QRC_PREFIX = '/qlementine/icons'

FREEDESKTOP_MAPPING_PATH = 'sources/FreeDesktopMappings.json'


def to_pascal_case(s: str) -> str:
  return re.sub(r'(_|-|\s)+', ' ', s).title().replace(' ', '')


def get_enum_key(file_path: str) -> str:
  match = re.match(HPP_ENUM_NAME_REGEX, file_path)
  if match:
    dirs = match.group(1)
    dirs = dirs.split('/')
    dirs = map(to_pascal_case, dirs)
    dirs = '_'.join(dirs)

    file = match.group(2)
    file = file.removesuffix('.svg')
    file = to_pascal_case(file)

    return dirs + file
  else:
    print(f'Cannot parse enum item name for: "{file_path}"')
    sys.exit(1)


def get_template(file_path: str) -> Template:
  with open(file_path, 'r') as f:
    template_txt = f.read()

  return Template(template_txt)


def build_icon_lists(icons_dir: str) -> dict[str, list[str]]:
  icon_lists = {}

  # Categories
  categories = [f for f in os.scandir(icons_dir) if f.is_dir()]
  categories.sort(key=lambda x: x.name)
  for category in categories:
    category_name = category.name
    # SVG files
    svg_files = [f for f in os.scandir(category.path) if f.is_file(
    ) and f.name.endswith('.svg')]
    svg_files.sort(key=lambda x: x.name.split('.')[0])
    for svg_file in svg_files:
      file_list: list[str] = icon_lists.setdefault(category_name, [])
      file_list.append(svg_file.name)

  return icon_lists


def write_qrc_file(icons_dir: str, category: str, items: list[str], qrc_prefix: str) -> str:

  qrc_items = map(lambda x: f'<file>{category}/{x}</file>', items)
  qrc_items_str = '\n    '.join(qrc_items)

  dir_name = pathlib.Path(icons_dir).name
  qrc_prefix = qrc_prefix + '/' + dir_name

  # Write file using the template.
  file_content = get_template(QRC_TEMPLATE_FILEPATH).substitute(
    qrc_prefix=qrc_prefix,
    qrc_items=qrc_items_str,
  )
  file_name = qrc_prefix.replace(
    '/', '_').lower()[1:] + '_' + category + '.qrc'
  file_path = os.path.join(icons_dir, file_name)

  with open(file_path, 'w') as f:
    f.write(file_content)

  return file_path


def write_enum_hpp_file(icon_lists: dict[str, list[str]], enum_name: str, output_filepath: str, qrc_path_base: str) -> None:
  # Prepare data for the template.
  enum_count = 1  # 'None' is already added in the template.
  enum_keys = []
  array_items = []
  for category, items in icon_lists.items():
    for item in items:
      enum_count += 1
      enum_keys.append(get_enum_key(f'{category}/{item}'))
      array_items.append(f'":{qrc_path_base}/{category}/{item}"')

  # Write file using the template.
  template_result = get_template(HPP_ENUM_TEMPLATE_FILEPATH).substitute(
     enum_name=enum_name,
     enum_keys=',\n'.join(enum_keys),
     enum_count=enum_count,
     array_items=',\n'.join(array_items)
  )
  with open(output_filepath, 'w') as f:
    f.write(template_result)

  # Run clang-format on file.
  call(['clang-format', '-i', output_filepath])


def get_freedesktop_map_lines(mapping_filepath: str) -> list[str]:
  with open(mapping_filepath, 'r') as file:
    data = json.load(file)

  map_lines: list[str] = []

  for key, value in data.items():
    if value:
      line = f'{{ "{key}", "{value}" }},'
      map_lines.append(line)

  return map_lines


def modify_cpp_file(qrc_init_lines: list[str], map_lines: list[str], cpp_filepath: str) -> None:
  with open(cpp_filepath, 'r') as f:
    cpp_content = f.read()

  # qrc
  replacement_qrc = r'\1\n  {}\n  \3'.format('\n  '.join(qrc_init_lines))
  new_cpp_content = re.sub(CPP_REGEXP_QRC, replacement_qrc, cpp_content)

  # map
  replacement_map = r'\1\n  {}\n  \3'.format('\n  '.join(map_lines))
  new_cpp_content = re.sub(CPP_REGEXP_MAP, replacement_map, new_cpp_content)

  with open(cpp_filepath, 'w') as f:
    f.write(new_cpp_content)


def update():
  print(f'Updating Qt file(s)...')

  qrc_init_lines: list[str] = []
  map_lines = get_freedesktop_map_lines(FREEDESKTOP_MAPPING_PATH)

  dirs = [f for f in os.scandir(ICONS_DIR) if f.is_dir()]
  dirs.sort(key=lambda d: d.path)
  for dir in dirs:
    dir_path = dir.path

    # Get lists of files from disk.
    icon_lists = build_icon_lists(dir_path)

    # Modify QRC files.
    for category, items in icon_lists.items():
      file_path = write_qrc_file(dir_path, category, items, QRC_PREFIX)
      print(f'Updated {file_path}')

      # Line to be added to cpp file.
      qrc_init_func_name = pathlib.Path(file_path).name.split('.')[0]
      qrc_init_lines.append(f'Q_INIT_RESOURCE({qrc_init_func_name});')

    # Modify HPP file that contains the C++ enum.
    enum_name = 'Icons' + dir.name
    hpp_filepath = HPP_ENUM_DIR + enum_name + '.hpp'
    qrc_path_base = QRC_PREFIX + '/' + dir.name
    write_enum_hpp_file(icon_lists, enum_name, hpp_filepath, qrc_path_base)
    print(f'Updated {hpp_filepath}')

  # Modify CPP file.
  # NB: CMake file doesn't need modification as it globs all .qrc files.
  modify_cpp_file(qrc_init_lines, map_lines, CPP_FILEPATH)
  print(f'Updated {CPP_FILEPATH}')

  print(f'Done updating Qt file(s).\n')


if __name__ == "__main__":
  update()
