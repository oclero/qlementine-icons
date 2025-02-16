import os
from ruamel.yaml import YAML

ICONS_DIR = 'sources/resources/icons'

METADATA_FILE = 'docs/data/icons.yaml'

TMP_METADATA_FILE = 'docs/data/icons-tmp.yaml'

yaml = YAML()


def get_old_data(metadata_file: str) -> dict:
  with open(metadata_file, 'r') as file:
    yaml_content = yaml.load(file)
  icon_list = yaml_content['icons']

  icon_dict = {}
  for element in icon_list:
    if element['name'] == '':
      continue
    if element['path'] == '':
      continue

    value = {
      'path': element['path'],
    }
    if element['tags'] != []:
      value['tags'] = sorted(element['tags'])
    if 'freedesktop' in element and element['freedesktop'] != '':
      value['freedesktop'] = element['freedesktop']

    icon_dict[element['name']] = value

  return icon_dict


def get_new_data(icons_dir: str) -> dict:
  def is_hidden(file: str) -> bool:
    return file.startswith('.')

  icon_dict = {}
  for root, _, files in os.walk(icons_dir):
    files = [f for f in files if not is_hidden(f) and f.endswith('.svg')]
    for file in files:
      full_path = os.path.join(root, file).replace('\\', '/')
      head, _ = os.path.split(full_path)
      first_directory = os.path.basename(head)
      relative_path = os.path.relpath(head, icons_dir)
      file_name_wo_ext = os.path.splitext(os.path.basename(file))[0]
      icon_dict[file_name_wo_ext] = {
        'path': f'{relative_path}/{file}',
        'tags': [first_directory]
      }

  return icon_dict


def write_yaml(data: dict, metadata_file: str):
  with open(metadata_file, 'w') as file:
    yaml.dump(
      data, file)


def get_merged_data(old_data: dict, new_data: dict):
  # Remove keys from old_data that are not present in new_data.
  old_data_wo_deprecated = {key: value for key,
                            value in old_data.items() if key in new_data}

  # Merge
  merged_data = {**new_data, **old_data_wo_deprecated}
  return merged_data


def get_yaml_content(merged_data: dict):
  icon_list = []
  for key, value in merged_data.items():
    list_item = {
      'name': key,
      'path': value['path'].replace('\\', '/'),
      'tags': sorted(value['tags'])
    }
    if 'freedesktop' in value:
      list_item['freedesktop'] = value['freedesktop']

    icon_list.append(list_item)

  icon_list = sorted(icon_list, key=lambda x: x['name'])

  return {
    'icons': icon_list
  }


def update():
  print('Updating Hugo file(s)...')
  old_data = get_old_data(METADATA_FILE)
  new_data = get_new_data(ICONS_DIR)
  merged_data = get_merged_data(old_data, new_data)
  result = get_yaml_content(merged_data)
  write_yaml(result, METADATA_FILE)
  print(f'Updated {METADATA_FILE}')
  print('Done updating Hugo file(s).\n')
