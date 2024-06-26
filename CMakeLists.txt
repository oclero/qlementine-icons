cmake_minimum_required(VERSION 3.17.5)

# Set project information.
project("qlementine_icons"
  LANGUAGES CXX
  VERSION 1.2.0.0
)

# Global flags.
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set_property(GLOBAL PROPERTY USE_FOLDERS ON)

# Find Qt.
find_package(QT NAMES Qt6 Qt5 COMPONENTS Core Widgets Svg REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core Widgets Svg REQUIRED)

# Library.
add_subdirectory(sources)

# Sandbox.
if(${CMAKE_PROJECT_NAME} STREQUAL ${PROJECT_NAME})
  add_subdirectory(sandbox)
endif()
