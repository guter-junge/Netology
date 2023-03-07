from pprint import pprint
import requests

def get_superheroes():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    target_heroes = []
    max_int = 0
    response = requests.get(url=url).json()
    for hero in response:
        if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
            target_heroes.append(hero)
    for hero in target_heroes:
        if hero['powerstats']['intelligence'] > max_int:
            max_int = hero['powerstats']['intelligence']
    print(f'Самый большой интеллект у персонажа {hero["name"]}, его показатель - {max_int}')

# get_superheroes()



class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get('href')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

# if __name__ == '__main__':
#     disk_file_path = 'Netology/new.txt'
#     token = ''
#     uploader = YaUploader(token=token)
#     result = uploader.upload(disk_file_path=disk_file_path,
#                              filename="/Users/elisei/PycharmProjects/http_homework/venv/new.txt")



def stack_api():
    url = 'https://api.stackexchange.com/2.3/questions?todate=1677974400&order=desc&max=1678147200&sort=activity&site=stackoverflow'
    response = requests.get(url=url).json()
    target_questions = []
    for question in response['items']:
        if 'python' in question['tags']:
            target_questions.append(question)
    pprint(target_questions)

stack_api()