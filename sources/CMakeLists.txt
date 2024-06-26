# Create the library.
add_library(${PROJECT_NAME} STATIC)
add_library(oclero::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

file(GLOB_RECURSE QRC_FILES "resources/icons/*.qrc")
file(GLOB_RECURSE HPP_FILES "include/oclero/qlementine/icons/*.hpp")
file(GLOB_RECURSE CPP_FILES "src/icons/*.cpp")

target_sources(${PROJECT_NAME}
  PRIVATE
    ${HPP_FILES}
    ${CPP_FILES}
    ${QRC_FILES}
)

target_include_directories(${PROJECT_NAME}
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  PRIVATE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
)

target_link_libraries(${PROJECT_NAME} PRIVATE Qt::Core Qt::Svg)

set_target_properties(${PROJECT_NAME} PROPERTIES
  LINKER_LANGUAGE CXX
  AUTOMOC ON
  AUTORCC ON
  OUTPUT_NAME     ${PROJECT_NAME}
  PROJECT_LABEL   ${PROJECT_NAME}
  SOVERSION       ${PROJECT_VERSION_MAJOR}
  VERSION         ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
  DEBUG_POSTFIX   _debug
)

target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
