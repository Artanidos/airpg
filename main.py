#############################################################################
# Copyright (C) 2019 Olaf Japp
#
# This file is part of AI-RPG.
#
#  AI-RPG is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  AI-RPG is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with AI-RPG.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QCoreApplication.setOrganizationName("Artanidos")
    QCoreApplication.setApplicationName("AI-RPG")
    QCoreApplication.setApplicationVersion("1.0.0")

    app.setWindowIcon(QIcon("images/logo.svg"))

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
