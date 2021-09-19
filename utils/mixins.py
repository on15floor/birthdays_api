import decimal
import json
from datetime import date, datetime


def decimal_datetime_repr(obj):
    """ Tries to represent datetime and decimal objects as JSON-serializable equivalents """
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    elif isinstance(obj, datetime):
        return obj.strftime('%d.%m.%Y %H:%M:%S.%f')
    elif isinstance(obj, date):
        return obj.strftime('%d.%m.%Y')
    raise TypeError


class WriteJSONMixin:
    def jwrite(self, payload, payload_for_logging=None):
        """ Write JSON output to response body """
        self.set_header("Content-Type", 'application/json; charset="utf-8"')
        formatted = json.dumps(payload, ensure_ascii=False, default=decimal_datetime_repr)
        self.write(formatted)

        if payload_for_logging:
            self._data_out = payload_for_logging
        else:
            self._data_out = json.loads(formatted)
