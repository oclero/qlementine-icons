#!/usr/bin/env python3

import os
import re
from scour.scour import start as scour, parse_args as scour_args, getInOut as scour_io
import tempfile
import pathlib

# Scour can't do in-place modification so we use a buffer file.
TMP_SVG_OUTPUT_FILE = os.path.join(tempfile.gettempdir(), 'tmp.svg')

DEFAULT_COLOR = "#000"


def process_svg_file(input_path: str, output_path: str, change_color=True, new_color=DEFAULT_COLOR):
  # Ensure the destination dir exists.
  os.makedirs(os.path.dirname(output_path), exist_ok=True)
  # Create Scour options.
  scour_options = scour_args()
  # General.
  scour_options.infilename = input_path
  scour_options.outfilename = TMP_SVG_OUTPUT_FILE
  # Optimization.
  scour_options.digits = 3
  scour_options.simple_colors = True
  scour_options.style_to_xml = False
  # scour_options.group_collapse = True
  scour_options.group_create = False
  scour_options.keep_editor_data = False
  scour_options.keep_defs = False
  # SVG Document.
  scour_options.strip_xml_prolog = True
  scour_options.remove_titles = True
  scour_options.remove_descriptions = True
  scour_options.remove_metadata = True
  scour_options.remove_descriptive_elements = True
  scour_options.strip_comments = True
  scour_options.embed_rasters = False
  scour_options.enable_viewboxing = True
  # Output formatting.
  scour_options.indent_type = 'none'
  scour_options.newlines = False
  scour_options.strip_xml_space_attribute = True
  # ID attributes.
  scour_options.strip_ids = True
  (scour_input, scour_output) = scour_io(scour_options)

  # Write file.
  scour(scour_options, scour_input, scour_output)

  # Replace all white by black.
  with open(TMP_SVG_OUTPUT_FILE, 'r') as f:
    file_content = f.read()

  if change_color:
    file_content = re.sub(r'="#f+"', f'="{new_color}"', file_content)

  with open(output_path, 'w') as f:
    f.write(file_content)


def process_svg_folder(svg_dir_path: str, overwrite=True, change_color=True, new_color=DEFAULT_COLOR) -> int:
  count = 0
  for root, _, files in os.walk(svg_dir_path):
    files = [f for f in files if not f.startswith(
      '.') and f.endswith('.svg')]
    for file in files:
      input_path = os.path.join(root, file)
      output_path = input_path if overwrite else os.path.join(
        svg_dir_path, 'compressed', file)
      process_svg_file(input_path, output_path, change_color, new_color)
      count = count + 1

  # Remove temporary file.
  if os.path.exists(TMP_SVG_OUTPUT_FILE):
    os.remove(TMP_SVG_OUTPUT_FILE)

  return count


def get_icons_dir() -> str:
  root_dir = pathlib.Path(__file__).parent.parent.absolute().as_posix()
  icons_dir = os.path.join(root_dir, 'sources/resources/icons')
  return icons_dir


if __name__ == '__main__':
  print('Optimizing SVG files...')
  icons_dir = get_icons_dir()
  new_color = DEFAULT_COLOR
  count = process_svg_folder(
    icons_dir, overwrite=True, change_color=True, new_color=new_color)
  print(f'Done optimizing {count} SVG file(s).\n')
