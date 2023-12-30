#!/usr/bin/env python3

import update_qt_files
import update_hugo_files

if __name__ == "__main__":
  print('Updating file(s)...\n')
  update_qt_files.update()
  update_hugo_files.update()
  print('Done.')
