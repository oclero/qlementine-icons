set(SANDBOX_NAME "sandbox")

qt_add_executable(${SANDBOX_NAME} WIN32 MACOSX_BUNDLE
  ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp
)

target_link_libraries(${SANDBOX_NAME}
  PRIVATE
    Qt::Widgets
    qlementine-icons
)

install(
  TARGETS ${SANDBOX_NAME}
  BUNDLE DESTINATION .
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

set_target_properties(${SANDBOX_NAME}
  PROPERTIES
    INTERNAL_CONSOLE OFF
    EXCLUDE_FROM_ALL OFF
    FOLDER "tools"
    CMAKE_AUTOMOC ON
    CMAKE_AUTORCC ON
    CMAKE_AUTOUIC ON
    MACOSX_BUNDLE_GUI_IDENTIFIER "oclero.qlementine-icons.sandbox"
)
