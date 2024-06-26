import os
import re
import pathlib
import sys
from string import Template
from subprocess import call


def this_dir_path():
  return pathlib.Path(__file__).parent.absolute().as_posix()


ICONS_DIR = 'sources/resources/icons/16'

CPP_FILEPATH = 'sources/src/icons/QlementineIcons.cpp'
CPP_REGEXP = r'(\/\/ ---.*)\s+((?:.*\n)*)\s+(\/\/ ---)'
CPP_QRC_INIT_TEMPLATE = 'Q_INIT_RESOURCE({});'

HPP_ENUM_NAME = 'Icons16'
HPP_ENUM_FILEPATH = 'sources/include/oclero/qlementine/icons/' + HPP_ENUM_NAME + '.hpp'
HPP_ENUM_NAME_REGEX = r'(.*\/)(.*\.svg)'
HPP_ENUM_TEMPLATE_FILEPATH = this_dir_path() + '/resources/Template.hpp'

QRC_PREFIX = '/qlementine/icons/16'
QRC_TEMPLATE_FILEPATH = this_dir_path() + '/resources/Template.qrc'
QRC_ITEM_TEMPLATE = '<file alias="{}">{}</file>'
QRC_NAME_TEMPLATE = 'qlementine_icons_16_{}'
QRC_FILENAME_TEMPLATE = QRC_NAME_TEMPLATE + '.qrc'


def is_hidden(file: str) -> bool:
  return file.startswith('.')


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


class IconData:
  enum_key: str = ''
  qrc_alias: str = ''
  qrc_filepath: str = ''

  def __init__(self, enum_key: str, qrc_alias: str, qrc_filepath: str):
    self.enum_key = enum_key
    self.qrc_alias = qrc_alias
    self.qrc_filepath = qrc_filepath

  def __lt__(self, other) -> bool:
    return self.enum_key < other.enum_key

  def __str__(self):
    return self.qrc_filepath


def build_icon_lists(icons_dir: str) -> dict[str, list[IconData]]:
  icon_lists = {}
  for root, _, files in os.walk(icons_dir):

    files = [f for f in files if not is_hidden(f) and f.endswith('.svg')]

    for file in files:
      full_path = os.path.join(root, file)
      head, tail = os.path.split(full_path)
      dir = os.path.split(head)[-1]
      rel_path = os.path.join(dir, tail)

      file_list: list[IconData] = icon_lists.setdefault(dir, [])

      file_list.append(IconData(get_enum_key(rel_path), tail, rel_path))

  for category, items in icon_lists.items():
    icon_lists[category] = sorted(items)

  return dict(sorted(icon_lists.items()))


def write_qrc_file(category: str, items: list[IconData], icons_dir: str) -> str:

  qrc_items = map(lambda x: QRC_ITEM_TEMPLATE.format(
    x.qrc_alias, x.qrc_filepath), items)
  qrc_items = '\n    '.join(qrc_items)

  # Write file using the template.
  qrc_template = get_template(QRC_TEMPLATE_FILEPATH)
  file_content = qrc_template.substitute(
    qrc_prefix=QRC_PREFIX,
    qrc_items=qrc_items,
  )
  file_path = os.path.join(icons_dir, QRC_FILENAME_TEMPLATE.format(category))
  with open(file_path, 'w') as f:
    f.write(file_content)

  return file_path


def write_enum_hpp_file(icon_lists: dict[str, list[IconData]], enum_name: str, output_filepath: str) -> None:
  # Prepare data for the template.
  enum_count = 1
  enum_keys = []
  array_items = []
  for qrc_list in icon_lists.values():
    for qrc_list_item in qrc_list:
      enum_count += 1
      enum_keys.append(qrc_list_item.enum_key)
      array_items.append(f'":/qlementine/icons/{qrc_list_item.qrc_alias}"')

  # Write file using the template.
  hpp_enum_template = get_template(HPP_ENUM_TEMPLATE_FILEPATH)
  template_result = hpp_enum_template.substitute(
     enum_name=enum_name,
     enum_keys=',\n'.join(enum_keys),
     enum_count=enum_count,
     array_items=',\n'.join(array_items)
  )
  with open(output_filepath, 'w') as f:
    f.write(template_result)

  # Run clang-format on file.
  call(['clang-format', '-i', output_filepath])


def modify_cpp_file(icon_lists: dict, cpp_filepath: str) -> None:
  with open(cpp_filepath, 'r') as f:
    cpp_content = f.read()

  qrc_inits = [CPP_QRC_INIT_TEMPLATE.format(
    QRC_NAME_TEMPLATE.format(x)) for x in icon_lists]
  replacement = r'\1\n  {}\n  \3'.format('\n  '.join(qrc_inits))
  new_cpp_content = re.sub(CPP_REGEXP, replacement, cpp_content)

  with open(cpp_filepath, 'w') as f:
    f.write(new_cpp_content)


def update():
  print(f'Updating Qt file(s)...')
  # Get lists of files from disk.
  icon_lists = build_icon_lists(ICONS_DIR)

  # Modify QRC files.
  for category, items in icon_lists.items():
    file_path = write_qrc_file(category, items, ICONS_DIR)
    print(f'Updated {file_path}')

  # Modify CPP file.
  # NB: CMake file doesn't need modification as it globs all .qrc files.
  modify_cpp_file(icon_lists, CPP_FILEPATH)
  print(f'Updated {CPP_FILEPATH}')

  # Modify HPP file that contains the C++ enum.
  write_enum_hpp_file(icon_lists, HPP_ENUM_NAME, HPP_ENUM_FILEPATH)
  print(f'Updated {HPP_ENUM_FILEPATH}')

  print(f'Done updating Qt file(s).\n')


if __name__ == "__main__":
  update()
