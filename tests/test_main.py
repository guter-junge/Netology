import unittest

from tests.tests_howework_main import geo_logs_rus, query_length, biggest_sales, check_folder_creation
import pytest

class Test_functions:

    @pytest.mark.parametrize('input, expected', [
        (
            [
                {'visit1': ['Москва', 'Россия']},
                {'visit2': ['Дели', 'Индия']},
                {'visit3': ['Владимир', 'Россия']},
                {'visit4': ['Лиссабон', 'Португалия']},
                {'visit5': ['Париж', 'Франция']},
                {'visit6': ['Лиссабон', 'Португалия']},
                {'visit7': ['Тула', 'Россия']},
                {'visit8': ['Тула', 'Россия']},
                {'visit9': ['Курск', 'Россия']},
                {'visit10': ['Архангельск', 'Россия']}
            ],
            [
                {'visit1': ['Москва', 'Россия']},
                {'visit3': ['Владимир', 'Россия']},
                {'visit7': ['Тула', 'Россия']},
                {'visit8': ['Тула', 'Россия']},
                {'visit9': ['Курск', 'Россия']},
                {'visit10': ['Архангельск', 'Россия']}
            ]
        ),
        (
            [],
            []
        )
    ]
                             )

    def test_geo_logs(self, input, expected):

        result = geo_logs_rus(input)

        assert result == expected
        assert len(result) == len(expected)

        for element in result:
            assert element[list(element.keys())[0]][1] == 'Россия'

    @pytest.mark.parametrize('input, expected', [
        (
                [
                    'смотреть сериалы онлайн',
                    'новости спорта',
                    'афиша кино',
                    'курс доллара',
                    'сериалы этим летом',
                    'курс по питону',
                    'сериалы про спорт'
                ],
                [
                    'Из 3 слов поисковых запросов 57.14%',
                    'Из 2 слов поисковых запросов 42.86%'
                ]
        ),
        (
                [],
                []
        ),
        (
            [
                'поиск 1',
                'поиск 2',
                23,
                'поиск 2 3'
            ],
            [
                'Из 2 слов поисковых запросов 50.0%',
                'Из 1 слов поисковых запросов 25.0%',
                'Из 3 слов поисковых запросов 25.0%'
            ]
        )
    ]
                             )

    def test_queries(self, input, expected):

        result = query_length(input)

        assert result == expected
        assert len(result) == len(expected)

    @pytest.mark.parametrize('input, expected', [
        (
                {
                    'facebook': 55,
                    'yandex': 120,
                    'vk': 115,
                    'google': 99,
                    'email': 42,
                    'ok': 98
                },
                'Больше всего продажи у yandex, их объем продаж равен 120'
        ),
        (
            {},
            ''
        ),
        (
                {
                    'facebook': -10000,
                    'yandex': -500000,
                    'google': 20
                },
                'Больше всего продажи у google, их объем продаж равен 20'
        )
    ]
                             )
    #
    def test_biggest_sales(self, input, expected):

        result = biggest_sales(input)

        assert result == expected

    @pytest.mark.parametrize('ya_token, disk_folder, expected', [
        (
            '',
            '/Test_folder/',
            ('Folder successfully created', 'Folder exists')
        )
    ]
                             )

    def test_ya_folder(self, ya_token, disk_folder, expected):

        result = check_folder_creation(ya_token, disk_folder)

        assert result == expected







