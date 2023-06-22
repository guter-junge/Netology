from application.salary import *
from application.db.people import *
from datetime import *

from data import *
from flatten_json import *

def flatten_json(dict):
    return flatten(dict)


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.today())

    print(flatten_json(data_dict))

