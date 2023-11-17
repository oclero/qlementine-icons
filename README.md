<div align="center">
<a href="https://oclero.github.io/qlementine-icons">
	<img style="margin-bottom: 2em;" src="docs/assets/img/thumbnail.png">
</a>
</div>

# Qlementine Icons

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://mit-license.org/)
[![CMake version](https://img.shields.io/badge/CMake-3.17+-064F8C?logo=cmake)](https://www.qt.io)
[![C++ version](https://img.shields.io/badge/C++-17-00599C?logo=++)](https://www.qt.io)
[![Qt5 version](https://img.shields.io/badge/Qt-5.15.2+-41CD52?logo=qt)](https://www.qt.io)
[![Qt6 version](https://img.shields.io/badge/Qt-6.0.0+-41CD52?logo=qt)](https://www.qt.io)

[![Linux](https://github.com/oclero/qlementine-icons/actions/workflows/linux.yml/badge.svg)](https://github.com/oclero/qlementine-icons/actions/workflows/linux.yml)

Vector icon set for modern desktop Qt5/Qt6 applications. Explore the icons on the [project's website](https://oclero.github.io/qlementine-icons).

---

### Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Author](#author)
- [License](#license)

---

## Features

- This repository is an icon set aimed to be used in conjunction with my Qt library named [Qlementine](https://github.com/oclero/qlementine).

- This icon set provides icons as requested by the [Freedesktop standard](http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html), and vastly expands it, in `16`×`16` pixels.

  > **Note:** Freedesktop coverage is a work in progress. Follow the progress [here](https://docs.google.com/spreadsheets/d/1lwPe_WPdQkgOCCKtCJghRR6EkeCQXrv96WzCUMdAfRE/edit?usp=sharing).

- The icons are in SVG format, so can be scaled to any size without loosing any quality. However, they've been designed to be used in `16`×`16` pixels, to be pixel-perfect.

- The icons are visible on the [project's website](https://oclero.github.io/qlementine-icons). Search among the library, and click on the icon to download the SVG file.

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
   target_link_libraries(your_project oclero::qlementine_icons)
   ```

5. Initialize the library.

   ```c++
   #include <oclero/qlementine/icons/QlementineIcons.hpp>

   oclero::qlementine::icons::initializeIconTheme();
   ```

6. Define the **icon theme** on your `QApplication`.

   ```c++
   QIcon::setThemeName("qlementine");
   ```

7. When you want to retrieve an icon, you can use one of these methods:

   1. With `QIcon::fromTheme()`, by using the icon name.

      ```c++
      const auto icon = QIcon::fromTheme("redo");
      const auto pixmap = icon.pixmap(QSize(16, 16));
      ```

   2. With `QIcon::fromTheme()`, by using the Freedesktop standard identifier, **if the icon has one**.

      ```c++
      const auto iconName = oclero::qlementine::icons::fromFreeDesktop("edit-redo");
      const auto icon = QIcon::fromTheme(iconName);
      const auto pixmap = icon.pixmap(QSize(16, 16));
      ```

   3. With `QPixmap`. Note that the resulting image will be `16`×`16` pixels.

      ```c++
      const auto pixmap = QPixmap(":/qlementine/icons/redo.svg");
      ```

   4. With `QIcon`, to get any size.

      ```c++
      const auto icon = QIcon(":/qlementine/icons/redo.svg");
      const auto pixmap = icon.pixmap(QSize(64, 64));
      ```

## Author

**Olivier Cléro** | [email](mailto:oclero@pm.me) | [website](https://www.olivierclero.com) | [github](https://www.github.com/oclero) | [gitlab](https://www.gitlab.com/oclero)

## License

**Qlementine Icons** is available under the MIT license. See the [LICENSE](LICENSE) file for more info.
