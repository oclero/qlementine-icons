#include <QApplication>
#include <QWidget>
#include <QBoxLayout>
#include <QLabel>
#include <QIcon>

#include <memory>

#include <oclero/qlementine/icons/QlementineIcons.hpp>

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
  const QPixmap pixmap1(":/qlementine/icons/redo.svg");

  // METHOD 2: Get the image from an icon. You can get the size you want.
  const QPixmap pixmap2 = QIcon(":/qlementine/icons/redo.svg").pixmap(QSize(32, 32));

  // METHOD 3: Get the image from the icon theme. You can also get the size you want.
  const auto iconName = oclero::qlementine::icons::fromFreeDesktop("edit-redo");
  const QPixmap pixmap3 = QIcon::fromTheme(iconName).pixmap(QSize(64, 64));

  // Display the images.
  for (const auto& pixmap : { &pixmap1, &pixmap2, &pixmap3 }) {
    auto* label = new QLabel(window.get());
    label->setFixedSize(pixmap->size());
    label->setPixmap(*pixmap);
    layout->addWidget(label);
  }

  // Show the window.
  window->show();

  return qApplication.exec();
}
