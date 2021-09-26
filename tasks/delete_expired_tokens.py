from datetime import datetime
from utils.database import SQLite3Instance
from utils.decorators import print_func_duration


@print_func_duration
def del_exp_tokens():
    db = SQLite3Instance()
    where_condition = f'WHERE token_expired < "{datetime.now()}"'
    exp_tokens = db.select('users_tokens', [], where=where_condition)
    exp_tokens_ids = [d['id'] for d in exp_tokens]
    if exp_tokens_ids:
        for i in exp_tokens_ids:
            where_condition = f'WHERE id={i}'
            db.delete('users_tokens', where_condition)
            print(f'[i]> raw with id={i} deleted')
    else:
        print(f'[i]> nothing to deleted')


if __name__ == '__main__':
    del_exp_tokens()
