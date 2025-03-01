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

|  Branch  | Build                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `master` | [![Linux](https://github.com/oclero/qlementine-icons/actions/workflows/linux.yml/badge.svg?branch=master)](https://github.com/oclero/qlementine-icons/actions/workflows/linux.yml) [![Windows](https://github.com/oclero/qlementine-icons/actions/workflows/windows.yml/badge.svg?branch=master)](https://github.com/oclero/qlementine-icons/actions/workflows/windows.yml) [![MacOS](https://github.com/oclero/qlementine-icons/actions/workflows/macos.yml/badge.svg?branch=master)](https://github.com/oclero/qlementine-icons/actions/workflows/macos.yml) |
|  `dev`   | [![Linux](https://github.com/oclero/qlementine-icons/actions/workflows/linux.yml/badge.svg?branch=dev)](https://github.com/oclero/qlementine-icons/actions/workflows/linux.yml) [![Windows](https://github.com/oclero/qlementine-icons/actions/workflows/windows.yml/badge.svg?branch=dev)](https://github.com/oclero/qlementine-icons/actions/workflows/windows.yml) [![MacOS](https://github.com/oclero/qlementine-icons/actions/workflows/macos.yml/badge.svg?branch=dev)](https://github.com/oclero/qlementine-icons/actions/workflows/macos.yml)          |

Vector icon set for modern desktop Qt5/Qt6 applications. Browse the 350+ icons on the [project's website](https://oclero.github.io/qlementine-icons).

> **Need more icons?** Commissions for new icons (free or commercial) are possible. See below.

---

### Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Scripts](#scripts)
- [Website](#website)
- [Author](#author)
- [License](#license)

---

## Features

- This repository is an icon set aimed to be used in conjunction with my Qt library named [Qlementine](https://github.com/oclero/qlementine).

- This icon set provides icons as requested by the [Freedesktop standard](http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html), and vastly expands it, in `16`×`16` pixels.

  > **Note:** Freedesktop coverage is a work in progress. Follow the progress [here](https://docs.google.com/spreadsheets/d/1lwPe_WPdQkgOCCKtCJghRR6EkeCQXrv96WzCUMdAfRE/edit?usp=sharing).

- The icons are in SVG format, so can be scaled to any size without loosing any quality. However, they've been designed to be used in `16`×`16` pixels, to be pixel-perfect.

- The icons are visible on the [project's website](https://oclero.github.io/qlementine-icons). Search among the library, and click on the icon to download the SVG file.

- Commissions are possible if you need some icons. See [License](#license) below for more details.

## Usage

1. Add the library as a dependency with CMake FetchContent.

   ```bash
   include(FetchContent)
   FetchContent_Declare(qlementine-icons GIT_REPOSITORY "https://github.com/oclero/qlementine-icons.git")
   FetchContent_MakeAvailable(qlementine-icons)
   ```

2. Link with the library in CMake.

   ```cmake
   target_link_libraries(your_project qlementine-icons)
   ```

3. Initialize the library.

   ```c++
   #include <oclero/qlementine/icons/QlementineIcons.hpp>

   oclero::qlementine::icons::initializeIconTheme();
   ```

4. Define the **icon theme** on your `QApplication`.

   ```c++
   QIcon::setThemeName("qlementine");
   ```

5. When you want to retrieve an icon, you can use one of these methods:

   1. With `QIcon::fromTheme()`, by using the icon name.

      ```c++
      const auto icon = QIcon::fromTheme("action/redo");
      const auto pixmap = icon.pixmap(QSize(16, 16));
      ```

   2. With `QIcon::fromTheme()`, by using the Freedesktop standard identifier, **if the icon has one**.

      ```c++
      const auto iconName = fromFreeDesktop("edit-redo");
      const auto icon = QIcon::fromTheme(iconName);
      const auto pixmap = icon.pixmap(QSize(16, 16));
      ```

   3. With `QPixmap`. Note that the resulting image will be `16`×`16` _physical_ pixels, so not adapted to High-Resolution screens.

      ```c++
      const auto pixmap = QPixmap(":/qlementine/icons/16/action/redo.svg");
      ```

   4. With `QIcon`, to get any size, and ensure it will have the correct pixel ratio to be displayed on the scree.

      ```c++
      const auto icon = QIcon(":/qlementine/icons/16/action/redo.svg");
      const auto pixmap = icon.pixmap(QSize(64, 64));
      ```

   5. You can also get the path from the icon identifier, in the enum `IconId`.
      **This is the recommended way because it avoids making typo mistakes**.

      ```c++
      const auto icon = QIcon(iconPath(Icons16::Action_Undo));
      const auto pixmap = icon.pixmap(QSize(16, 16));
      ```

## Scripts

Some Python scripts are in the `scripts` folder and are useful to manage the huge icon list.

### Updating the project files: `update.py`

```sh
update.py
```

This script will update the various files that depend on the icon list:

- **Qt files**

  1. The script creates the `.qrc` files based on the folder structure.
  2. In `sources/CMakeLists.txt`, cmake uses the `glob` function to get all the `.qrc` files, and will generate the appropriate C++ lines in `sources/src/icons/QlementineIcons.cpp`.

- **Hugo files**

  - The script keeps up-to-date the `docs/data/icons.yml` metadata file.
  - This file is used to generate at compile-time the HTML table.

### Optimizing the SVG files: `optimize_svg_files.py`

#### Usage

Put the SVG files you want to optimize in a `tmp` folder, then:

```sh
optimize_svg_files.py
```

This script will use the `scour` library to optimize SVG: stripping all unnecessary data and reducing the decimal count.

Please do not run it on already optimized files, because the rounding will change the decimal count, and Git will see a modification.

## Website

The documentation/showcase website is made with `hugo`. You can see a local preview at <http://localhost:1313/qlementine-icons> by executing:

```bash
hugo server --source ./docs
```

## Author

**Olivier Cléro** | [email](mailto:oclero@pm.me) | [website](https://www.olivierclero.com) | [github](https://www.github.com/oclero) | [gitlab](https://www.gitlab.com/oclero)

## License

**Qlementine Icons** is available under the MIT license. See the [LICENSE](LICENSE) file for more info.

If you or your company wants to use Qlementine Icons, but found out some icons are missing, here are some common cases:

1. **Free icons:** If the icons are general-purpose enough, I can made them **for free** and add them to this MIT-licensed icon library. **Please create a Github issue**, describing precisely your needs.

2. **Commercial icons:** If you want icons in this very same style, but don't want to add them to Qlementine Icons, **I can work as a freelance artist for you**, and make these icons. Feel free to contact me by email to talk about details.
