cmake_minimum_required(VERSION 3.17.5)

# Set project information.
project("qlementine_icons"
  LANGUAGES CXX
  VERSION 1.5.0.0
  DESCRIPTION "Modern icon theme for Qt applications."
)

# Global flags.
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set_property(GLOBAL PROPERTY USE_FOLDERS ON)

# Find Qt.
find_package(Qt6 REQUIRED COMPONENTS Core Widgets Svg)
qt_standard_project_setup()

# Library.
add_subdirectory(sources)

# Sandbox.
if(${CMAKE_PROJECT_NAME} STREQUAL ${PROJECT_NAME})
  add_subdirectory(sandbox)
endif()
