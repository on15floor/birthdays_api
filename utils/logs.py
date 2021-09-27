import logging
from config import API_DIR


async def save_log(log: dict) -> None:
    # Определяем порядок в логе
    fields_order = ['ip', 'uri', 'user_id', 'email', 'user-agent']
    log_line = '; '.join('%s: %s' % (f, log.pop(f)) for f in fields_order if f in log)

    logger = logging.getLogger('log')

    set_formatter = logging.Formatter('date: %(asctime)s.%(msecs)d; %(message)s', '%Y-%m-%dT%H:%M:%S')
    file_handler = logging.FileHandler(f'{API_DIR}/docs/logs.log')
    file_handler.setFormatter(set_formatter)
    logger.addHandler(file_handler)
    logger.info(log_line)
