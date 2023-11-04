import os
import re

ICONS_DIR = 'sources/resources/icons'

CPP_FILEPATH = 'sources/src/icons/QlementineIcons.cpp'
CPP_REGEXP = r'(\/\/ ---.*)\s+((?:.*\n)*)\s+(\/\/ ---)'

QRC_FILE_TEMPLATE = '''<!DOCTYPE RCC>
<RCC version="1.0">
  <qresource prefix="/{}">
    {}
  </qresource>
</RCC>
'''
QRC_ITEM_TEMPLATE = '<file alias="{}">{}</file>'
QRC_NAME_TEMPLATE = 'qlementine_icons_{}'
QRC_FILENAME_TEMPLATE = QRC_NAME_TEMPLATE + '.qrc'
QRC_INIT_TEMPLATE = 'Q_INIT_RESOURCE({});'


def build_qrc_lists(icons_dir: str):
  qrc_lists = {}
  for root, dirs, files in os.walk(icons_dir):
    def is_hidden(file):
      return file.startswith('.')
    files = [f for f in files if not is_hidden(f) and f.endswith('.svg')]

    for file in files:
      full_path = os.path.join(root, file)
      head, tail = os.path.split(full_path)
      dir = os.path.split(head)[-1]
      rel_path = os.path.join(dir, tail)

      file_list: list[str] = qrc_lists.setdefault(dir, [])

      item = QRC_ITEM_TEMPLATE.format(tail, rel_path)
      file_list.append(item)

  for category, category_list in qrc_lists.items():
    qrc_lists[category] = sorted(category_list)

  return dict(sorted(qrc_lists.items()))


def write_qrc_file(category: str, category_list: list[str], icons_dir: str):
  prefix = 'qlementine/icons/'
  items = '\n    '.join(category_list)
  file_content = QRC_FILE_TEMPLATE.format(prefix, items)
  file_path = os.path.join(icons_dir, QRC_FILENAME_TEMPLATE.format(category))
  with open(file_path, 'w') as f:
    f.write(file_content)
  return file_path


def modify_cpp_file(qrc_lists: dict, cpp_filepath: str):
  with open(cpp_filepath, 'r') as f:
    cpp_content = f.read()

  qrc_inits = [QRC_INIT_TEMPLATE.format(
    QRC_NAME_TEMPLATE.format(x)) for x in qrc_lists]
  replacement = r'\1\n  {}\n  \3'.format('\n  '.join(qrc_inits))
  new_cpp_content = re.sub(CPP_REGEXP, replacement, cpp_content)

  with open(cpp_filepath, 'w') as f:
    f.write(new_cpp_content)


def update():
  print(f'Updating Qt file(s)...')
  # Get lists of files from disk.
  qrc_lists = build_qrc_lists(ICONS_DIR)

  # Modify QRC files.
  for category, category_list in qrc_lists.items():
    file_path = write_qrc_file(category, category_list, ICONS_DIR)
    print(f'Updated {file_path}')

  # Modify CPP file.
  # NB: CMake file doesn't need modification as it globs all .qrc files.
  modify_cpp_file(qrc_lists, CPP_FILEPATH)
  print(f'Updated {CPP_FILEPATH}')
  print(f'Done updating Qt file(s).\n')
