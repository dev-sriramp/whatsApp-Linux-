import os
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineCore import (
    QWebEnginePage,
    QWebEngineDownloadRequest,
    QWebEngineProfile,
    QWebEngineSettings,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt, QUrl, QStandardPaths, QSettings, QLocale, QThreadPool
from PyQt6.QtCore import QEvent, Qt, QUrl, QSettings
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFileDialog, QMenu
import getTheme


class WhatsApp(QWebEnginePage):

    link_url = ""

    def __init__(self, *args, **kwargs):
        QWebEnginePage.__init__(self, *args, **kwargs)
        QApplication.instance().installEventFilter(self)
        self.featurePermissionRequested.connect(self.permission)
        self.linkHovered.connect(self.link_hovered)
        self.loadFinished.connect(self.load_finished)

    def load_finished(self, flag):
        if flag or not flag:
            self.runJavaScript(
                """
                const checkExist = setInterval(() => {
                    const classElement = document.getElementsByClassName("_1XkO3")[0];
                    if (classElement != null) {
                        classElement.style = 'max-width: initial; width: 100%; height: 100%; position: unset;margin: 0'
                        clearInterval(checkExist);
                    }
                }, 100);

                 const checkNotify = setInterval(() => {
                    const classElement = document.evaluate('//*[@id="side"]/span/div/div/div[2]/div[2]/span/span[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    if (classElement != null) {
                        classElement.click()
                        clearInterval(checkNotify);
                    }
                }, 100);
            """
            )
            settings = QSettings("WhatsApp For Linux", "WhatsApp For Linux", self)
            theme_mode = settings.value("system/theme", "auto", str)
            if theme_mode == "auto":
                self.setTheme(getTheme.get_system_theme())
            elif theme_mode == "light":
                self.setTheme(False)
            else:
                self.setTheme(True)

    def setTheme(self, isNight_mode):
        if isNight_mode == False:
            self.runJavaScript("document.body.classList.remove('dark')")
        else:
            self.runJavaScript("document.body.classList.add('dark')")

    def link_hovered(self, url):
        self.link_url = url

    def permission(self, frame, feature):
        self.setFeaturePermission(
            frame, feature, QWebEnginePage.PermissionPolicy.PermissionGrantedByUser
        )

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                if (
                    self.link_url != ""
                    and self.link_url != __whatsapp_url__
                    and not "faq.whatsapp.com/web/download-and-installation/how-to-log-in-or-out"
                    in self.link_url
                ):
                    QDesktopServices.openUrl(QUrl(self.link_url))
                    return True
        return False
