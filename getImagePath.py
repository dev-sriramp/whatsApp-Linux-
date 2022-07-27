def getPathImage(qin, title):
    """
    To show an image in notifications on dbus it is necessary that the image exists in a directory.
    So the contact image is saved in a temporary folder (tmp) in the application data folder
    """
    try:
        path = "/home/anonymous/Desktop/webWhatsApp/logo.png"

        qout = QImage(qin.width(), qin.height(), QImage.Format.Format_ARGB32)
        qout.fill(Qt.GlobalColor.transparent)

        brush = QBrush(qin)

        pen = QPen()
        pen.setColor(Qt.GlobalColor.darkGray)
        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)

        painter = QPainter(qout)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.drawRoundedRect(
            0, 0, qin.width(), qin.height(), qin.width() // 2, qin.height() // 2
        )
        painter.end()
        c = qout.save(path)
        if c == False:
            return "dev.sriramp.whatsappLinux"
        else:
            return path
    except:
        return "dev.sriramp.whatsappLinux"
