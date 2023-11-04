find_package(Qt${QT_DEFAULT_MAJOR_VERSION} COMPONENTS Widgets REQUIRED)

add_executable(sandbox WIN32 MACOSX_BUNDLE)

target_sources(sandbox PRIVATE
  ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp
)

target_link_libraries(sandbox
  PRIVATE
    Qt::Widgets
    oclero::qlementine_icons
)

set_target_properties(sandbox PROPERTIES
  INTERNAL_CONSOLE OFF
  EXCLUDE_FROM_ALL OFF
  FOLDER sandbox
  AUTOMOC ON
  AUTORCC ON
)
