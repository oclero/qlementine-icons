#include <QApplication>
#include <QWidget>
#include <QBoxLayout>
#include <QLabel>
#include <QIcon>

#include <memory>

#include <oclero/qlementine/icons/QlementineIcons.hpp>
#include <oclero/qlementine/icons/Icons16.hpp>

int main(int argc, char* argv[]) {
  // Must be set before creating a QApplication.
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
  QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling, true);
  QCoreApplication::setAttribute(Qt::AA_UseHighDpiPixmaps, true);
#endif

  QApplication qApplication(argc, argv);

  // Must be set after creating a QApplication.
  QGuiApplication::setApplicationDisplayName("sandbox");
  QCoreApplication::setApplicationName("sandbox");
  QGuiApplication::setDesktopFileName("sandbox");
  QCoreApplication::setOrganizationName("oclero");
  QCoreApplication::setOrganizationDomain("olivierclero.com");
  QCoreApplication::setApplicationVersion("1.0.0");
  QApplication::setHighDpiScaleFactorRoundingPolicy(Qt::HighDpiScaleFactorRoundingPolicy::PassThrough);

  // Initialize the icon theme.
  oclero::qlementine::icons::initializeIconTheme();

  // Define the icon theme.
  QIcon::setThemeName("qlementine");

  // Create the window.
  auto window = std::make_unique<QWidget>();
  window->setMinimumSize(320, 240);
  auto* layout = new QVBoxLayout(window.get());
  layout->setAlignment(Qt::AlignCenter);

  // METHOD 1: Get the image with a QPixmap. Its size will be the image's size.
  // Note: This won't get an image suited to the screen pixel ratio and might be blurry.
  const QPixmap pixmap1(":/qlementine/icons/16/action/redo.svg");

  // METHOD 2: Get the image from an icon. You can get the size you want.
  // Note: This will ensure an image with the correct pixel ratio (i.e. not blurry).
  const auto pixmap2 = QIcon(":/qlementine/icons/16/action/redo.svg").pixmap(QSize(32, 32));

  // METHOD 3: Get the image from the icon theme. You can also get the size you want.
  // Note: this will also get you an image with the correct pixel ratio.
  const auto iconName = oclero::qlementine::icons::fromFreeDesktop("edit-redo");
  const auto pixmap3 = QIcon::fromTheme(iconName).pixmap(QSize(64, 64));

  // METHOD 4: [RECOMMENDED] Get the image from its ID.
  const auto iconPath = oclero::qlementine::icons::iconPath(oclero::qlementine::icons::Icons16::Action_Undo);
  const auto pixmap4 = QIcon(iconPath).pixmap(QSize(16, 16));

  // Display the images.
  for (const auto& pixmap : { &pixmap1, &pixmap2, &pixmap3, &pixmap4 }) {
    auto* label = new QLabel(window.get());
    label->setFixedSize(pixmap->size());
    label->setPixmap(*pixmap);
    layout->addWidget(label);
  }

  // Show the window.
  window->show();

  return qApplication.exec();
}
