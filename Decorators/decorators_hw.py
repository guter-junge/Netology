import os
import datetime

def logger(old_function):
    path = 'main.log'
    def new_function(*args, **kwargs):
        date_time = str(datetime.datetime.now())
        # print(date_time)
        name = old_function.__name__
        result = old_function(*args, **kwargs)
        # if isinstance(result, float):
        complete_string = f'Function name - {name},\n' \
                   f'Date and time - {date_time},\n' \
                   f'Arguments - {args} and {kwargs},\n' \
                   f'Result - {result} \n'

        with open(path, 'a') as log_file:
            log_file.write(complete_string)

        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b
#
    # assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'

if __name__ == '__main__':
    test_1()

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            date_time = str(datetime.datetime.now())
            # print(date_time)
            name = old_function.__name__
            result = old_function(*args, **kwargs)
            # if isinstance(result, float):
            complete_string = f'Function name - {name},\n' \
                       f'Date and time - {date_time},\n' \
                       f'Arguments - {args} and {kwargs},\n' \
                       f'Result - {result} \n'

            with open(path, 'a') as log_file:
                log_file.write(complete_string)

            return result

        return new_function
    return __logger

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'

if __name__ == '__main__':
    test_2()