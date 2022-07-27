import os
import sys
from PyQt6.QtWidgets import QFileDialog, QMenu
from PyQt6.QtWebEngineCore import (
    QWebEnginePage,
    QWebEngineDownloadRequest,
    QWebEngineProfile,
    QWebEngineSettings,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt, QUrl, QStandardPaths, QSettings, QLocale, QThreadPool
from PyQt6.QtCore import QEvent, Qt, QUrl, QSettings
from PyQt6.QtGui import QDesktopServices, QIcon, QPalette
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFileDialog, QMenu


class Download(QWebEngineProfile):
    def __init__(self, *args, **kwargs):
        super(Download, self).__init__(*args, **kwargs)
        self.webview = QWebEngineView()

    def download(self, download):
        if (
            download.state()
            == QWebEngineDownloadRequest.DownloadState.DownloadRequested
        ):
            path, _ = QFileDialog.getSaveFileName(
                self, self.webview.tr("Save file"), download.downloadFileName()
            )
            if path:
                download.setDownloadDirectory(os.path.dirname(path))
                download.setDownloadFileName(os.path.basename(path))
                download.url().setPath(path)
                download.accept()
