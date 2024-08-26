import logging
class LoggingMixin:
    _log = None
    @property
    def log(self):
        if self._log is None:
            self._log = logging.getLogger('invivo_tests')
            self._set_logger()
        return self._log
    def _set_logger(self):
        self._log.setLevel(logging.INFO)
        fmt = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(funcName)s() - %(message)s'
        formatter = logging.Formatter(fmt)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self._log.addHandler(handler)
