'''
Creator : SeoJK
CreateTime : 2018.03.31

'''

import logging
from common import *

class MyLogger(Singleton):
    def __init__(self):
        self._logger = logging.getLogger("StockTrader")
        self._logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s (%(funcName)s) %(message)s')

        log_dir = "log"
        import os
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        from datetime import date
        today = date.today()
        filename = log_dir + "/" + today.strftime("%Y%m%d") + ".log"

        fileHandler = logging.FileHandler(filename, "a", "utf-8")
        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(self.formatter)
        streamHandler.setFormatter(self.formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

    def logger(self):
        return self._logger

    def SetLogView(self, widget):
        logTextBox = QPlainTextEditLogger(widget)
        logTextBox.setFormatter(self.formatter)
        self._logger.addHandler(logTextBox)


class QPlainTextEditLogger(logging.Handler):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)
