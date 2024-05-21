from bs4 import BeautifulSoup
import requests
import os

# URL страницы, которую вы хотите спарсить
url = "https://www.example.com"  # замените на нужный URL

# Папка для сохранения изображений
folder_path = "Faces"  # замените на нужный путь к папке

# Получение содержимого страницы
response = requests.get(url)
page_content = response.content

# Создание объекта BeautifulSoup для парсинга
soup = BeautifulSoup(page_content, 'html.parser')

# Нахождение всех блоков с классом "lister-item mode-detail"
blocks = soup.find_all('div', class_='lister-item mode-detail')

# Перебор блоков и извлечение информации
for block in blocks:
    # Извлечение имени и фамилии
    name_block = block.find('h3', class_='lister-item-header')
    name = name_block.find('a').text.strip()

    # Извлечение ссылки на картинку
    image_url = block.find('img')['src']

    # Создание пути для сохранения изображения
    image_path = os.path.join(folder_path, f"{name}.jpg")

    # Скачивание и сохранение изображения
    response = requests.get(image_url)
    with open(image_path, 'wb') as image_file:
        image_file.write(response.content)

    # Вывод информации
    print(f"Сохранено изображение для {name}")