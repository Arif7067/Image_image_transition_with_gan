import requests
import threading
import queue
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import os
from selenium.webdriver.common.keys import Keys
import time
import os
import time
from io import BytesIO

q = queue.Queue()
valid_proxies=[]

with open("check.txt","r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def get_images_from_google(delay, download_path):
    # URL of the image
    image_url = "https://tile.openstreetmap.org/18/{x}/{y}.png"

    x_range = range(77149, 77273)
    y_range = range(98530, 98639)  # Corrected the y_range

    # Loop through x and y values to fetch and save images
    for x in x_range:
        os.chdir(download_path)
        Newfolder = str(x)
        path = os.path.join(download_path, Newfolder)        
        if not os.path.exists(path):
            os.makedirs(path)        
        os.chdir(path)
        for y in y_range:
            file_name = f"{x}"

            # Create the URL for the specific tile by replacing {x} and {y}
            url = image_url.format(x=x, y=y)
#             webbrowser.open(url,new=1)
#             print(url)
#             headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        

            # Send an HTTP GET request to fetch the image
#         response = requests.get(url, headers=headers)
            response = requests.get(url)

            if response.status_code == 200:
                # Load the image from the response content
                img = Image.open(BytesIO(response.content))

                # Save the image to a file
                file_path = os.path.join(path, f"{y}.png")
                img.save(file_path, "PNG")
                time.sleep(delay)
                print("Success")

                # Optionally, you can resize or preprocess the image here for your ML task
            else:
                print(f"Failed to fetch image for tile ({x}, {y})")

    print("Image download and saving completed.")


Urls=get_images_from_google(0.1,"C:/Users/HP/Machinne Learning/webscraping_formap/open_18")