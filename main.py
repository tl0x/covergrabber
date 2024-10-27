import requests
from bs4 import BeautifulSoup
import os

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True)
        if not os.path.exists("out"):
            os.makedirs("out")
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):  
                    file.write(chunk)
            print(f"Image successfully downloaded: {save_path}")
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


url = input("Paste the link to the song: ")

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

img_tags = soup.find_all('img')
h1_tags = soup.find_all('h1')
title = ""
for i in h1_tags:
    title = i.get_text()

for img in img_tags:
    if img['loading'] == "eager":
        download_image(img['src'], "out/" + title + ".png")




