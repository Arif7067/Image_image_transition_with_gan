import requests
import threading
import queue
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
import time
from PIL import Image
import os
from selenium.webdriver.common.keys import Keys
import time


# Function to download images using Selenium WebDriver
def download_images_with_browser(delay, download_path):
    # URL pattern for the images
    image_url = "https://tile.openstreetmap.org/18/{x}/{y}.png"   #c.tile

    x_range = range(77149, 77273)
    y_range = range(98530, 98639)  # Adjust the range as needed

    # Set up the web browser (Chrome in this example)
    driver_path = "C:/Users/HP/Machinne Learning/webscraping_formap/driver/version_116/chromedriver"  # Specify the path to ChromeDriver
    driver = webdriver.Chrome(executable_path=driver_path)

    # Loop through x and y values to fetch and save images
    for x in x_range:
        os.chdir(download_path)
        Newfolder = str(x)
        path = os.path.join(download_path, Newfolder)
        
        if not os.path.exists(path):
            os.makedirs(path)        
        os.chdir(path)
        for y in y_range:
#             file_name = f"{x}"

            # Create the URL for the specific tile by replacing {x} and {y}
            url = image_url.format(x=x, y=y)

            # Open the web browser and navigate to the URL
            driver.get(url)

            # Wait for the image to load (you can adjust the sleep time as needed)
            time.sleep(2)

            # Find the image element on the web page
            image_element = driver.find_elements_by_tag_name("img")

            
            for index, image_element in enumerate(image_element):
                # Get the image source URL
                image_src = image_element.get_attribute("src")

            # Download the image using requests
                response = requests.get(image_src)
                if response.status_code == 200:
                    # Save the image to a file
                    file_path = os.path.join(path, f"{y}.png")
                    with open(file_path, "wb") as f:
                        f.write(response.content)

                    print(f"Downloaded image for tile ({x}, {y})")

                    # Optionally, you can resize or preprocess the image here for your ML task

                    # Delay between downloads (you can adjust this as needed)
                    time.sleep(delay)
                else:
                    print(f"Failed to fetch image for tile ({x}, {y})")

    # Close the web browser
    driver.quit()
    print("Image download and saving completed.")


download_images_with_browser(1, "C:/Users/HP/Machinne Learning/webscraping_formap/open_18")