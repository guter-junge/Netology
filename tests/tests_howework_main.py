import requests

def geo_logs_rus(input):


    geo_logs_new = []

    for element in input:
        for number, destination in element.items():
            if destination[1] == 'Россия':
                geo_logs_new.append(element)
            else:
                pass

    return geo_logs_new

def query_length(input):

    new_dict = {}

    for element in input:
        if type(element) == int:
            element = str(element)
            length = len(element.split(' '))
            new_dict[length] = new_dict.get(length, 0) + 1
        else:
            length = len(element.split(' '))
            new_dict[length] = new_dict.get(length, 0) + 1

    length_list = []
    for key, value in new_dict.items():
        length_list.append(f'Из {key} слов поисковых запросов {round((value / len(input) * 100), 2)}%')

    return length_list

def biggest_sales(input):

    max_count = 0
    company = None

    for name, sales in input.items():
        if sales > max_count:
            max_count = sales
            company = name
    if company != None and max_count != 0:
        return f'Больше всего продажи у {company}, их объем продаж равен {max_count}'
    else:
        return ''



class Ya_disk:

    url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def __init__(self, token, disk_folder):
        self.token = token
        self.disk_folder = disk_folder

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self):
        url = self.url
        headers = self.get_headers()
        params = {'path': f'{self.disk_folder}',  'overwrite': 'true'}
        response = requests.put(url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 201:
            return 'Folder successfully created'
        else:
            return f'Failed to create folder, {response.status_code}'

    def get_folders(self):
        url = self.url
        headers = self.get_headers()
        params = {'path': self.disk_folder, 'overwrite': 'true'}
        response = requests.get(url=url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 200:
            return 'Folder exists'
        else:
            return f"Folder doesn't exist, {response.status_code}"




def check_folder_creation(ya_token, disk_folder):
    ya = Ya_disk(token=ya_token, disk_folder=disk_folder)
    result1 = ya.create_folder().strip()
    result2 = ya.get_folders().strip()
    return result1, result2


if __name__ == '__main__':
    ya_token = 'y0_AgAAAAAgO2y6AADLWwAAAADdgCSvmx_rvQV7TBqikyfdY1xEzTnoRiU'
    disk_folder = '/Test_folder/'
    check_folder_creation(ya_token, disk_folder)
