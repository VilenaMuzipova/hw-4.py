import requests
import os
import json
import csv


def check_web():
    """ проверка апи"""
    req = requests.get(URL)
    print(req)

def get_all_info():
    """Вывод информации о всех пользователях"""
    print(json.loads(requests.get(URL).text))

def create_data_base_of_users():
    """Создание общей директории"""
    os.mkdir("DataBase")

def create_list_info_of_users():
    """Вывод информации о пользователе"""
    with open("DataBase/Users_6/info_of_user6.csv", "w", newLine='') as info_file:
        res = requests.get(URL)
        info = ras.json()
        result = (info["data"])
        fieldnames = ["id", "first_name", "last_name", "email", "avatar"]
        writer = csv.DictWriter(info_file, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerow(
            result
        )

    def create_avatar():
        """Создание автара пользователя"""
        avatar = requests.get("https://reqres.in/img/faces/6-image.jpg")
        with open (" ")as file:
            file.write(avatar.content)

    #точка входа
    if __name__ == "__main__"
        URL = "https://reqres.in/api/users"

    