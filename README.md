<div align="center">
	<img height="50" src="branding/logo.svg">
</div>

# Qlementine Icons

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://mit-license.org/)

Freedesktop icon set for modern desktop Qt5 applications.

---

### Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Author](#author)
- [License](#license)

---

## Features

This repository is an icon set aimed to be used in conjunction with my Qt library named [Qlementine](https://github.com/oclero/qlementine).

This icon set provides all the icons as requested by the [Freedesktop standard](http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html).

> **Note:** Work in progress. Follow the progress [here](https://docs.google.com/spreadsheets/d/1lwPe_WPdQkgOCCKtCJghRR6EkeCQXrv96WzCUMdAfRE/edit?usp=sharing).
>
> A release will be created when all the icons are made.

## Usage

1. Add the library's repository as a Git submodule.

   ```bash
   git submodule add git@github.com:oclero/qlementine-icons.git submodules/qlementine-icons
   ```

2. Download submodules.

   ```bash
   git submodule update --init --recursive
   ```

3. Add the library to your CMake project.

   ```cmake
   add_subdirectory(submodules/qlementine-icons)
   ```

4. Link with the library in CMake.

   ```cmake
   target_link_libraries(your_project oclero::qlementine)
   ```

5. Define the `QIcon` theme on your `QApplication`.

   ```c++
   QIcon::setThemeName("qlementine-icons");
   ```

6. When you want to retrieve an icon, use the standard identifier as defined by the Freedesktop specification.

   ```c++
   const auto icon = QIcon::fromTheme("edit-undo");
   ```

## Author

**Olivier Cléro** | [email](mailto:oclero@pm.me) | [website](https://www.olivierclero.com) | [github](https://www.github.com/oclero) | [gitlab](https://www.gitlab.com/oclero)

## License

**Qlementine Icons** is available under the MIT license. See the [LICENSE](LICENSE) file for more info.
