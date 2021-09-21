from datetime import datetime
from utils.database import SQLite3Instance
from utils.decorators import print_func_duration


@print_func_duration
def del_exp_tokens():
    db = SQLite3Instance()
    where_condition = f'WHERE token_expired < "{datetime.now()}"'
    exp_tokens = db.select('users_tokens', [], where=where_condition)
    exp_tokens_ids = [d['id'] for d in exp_tokens]
    for id in exp_tokens_ids:
        where_condition = f'WHERE id={id}'
        db.delete('users_tokens', where_condition)
        print(f'[i]> raw with id={id} deleted')
    else:
        print(f'[i]> nothing to deleted')


if __name__ == '__main__':
    del_exp_tokens()
