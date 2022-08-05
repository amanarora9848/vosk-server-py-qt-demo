#!/usr/bin/env python3

import asyncio
import sys
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

from sendwav import run_test_wav
from record_voice_send import record_sound


class InPython(QObject):
    @pyqtSlot(result=str)
    def record_sound_button(self):
        if record_sound():
            return asyncio.run(run_test_wav('ws://localhost:2700'))
        else:
            return "Try again..."


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    context = engine.rootContext()
    context.setContextProperty("main", engine)
    engine.load('voiceRecognition.qml')
    win = engine.rootObjects()[0]

    inPython = InPython()
    context.setContextProperty("voiceRecognizer", inPython)

    win.show()
    sys.exit(app.exec_())
