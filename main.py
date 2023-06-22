from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

from data import data_dict
from flatten_json import flatten

def flatten_json(dict):
    return flatten(dict)


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.today())

    print(flatten_json(data_dict))






