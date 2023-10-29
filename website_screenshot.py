from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os
import time

class WebpageScreenshotCapture:
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path

    def capture_screenshot(self):
        # Set default download folder for ChromeDriver
        download_folder = os.path.dirname(self.output_path)
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        prefs = {"download.default_directory": download_folder}

        # SELENIUM SETUP
        logging.getLogger('WDM').setLevel(logging.WARNING)  # Hide not so relevant webdriver-manager messages
        chrome_options = Options()
        chrome_options.headless = True
        chrome_options.add_argument("--no-sandbox")  # Add this option to run in headless mode without sandboxing
        chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage to prevent certain issues
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.implicitly_wait(15)  # Increase the implicit wait time for stability
        driver.maximize_window()
        driver.get(self.url)

        # Wait for the page to fully load (you can increase the sleep time if needed)
        time.sleep(5)
        
        self.save_screenshot(driver)

        driver.quit()

    def save_screenshot(self, driver):
        height, width = self.scroll_down(driver)
        driver.set_window_size(width, height)
        img_binary = driver.get_screenshot_as_png()
        img = Image.open(BytesIO(img_binary))
        img.save(self.output_path)
        print(f"Screenshot saved as '{self.output_path}'")
    """
    def scroll_down(self, driver):
        total_width = driver.execute_script("return document.body.scrollWidth")
        total_height = driver.execute_script("return document.body.scrollHeight")
        viewport_width = driver.execute_script("return window.innerWidth")
        viewport_height = driver.execute_script("return window.innerHeight")

        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                rectangles.append((ii, i, top_width, top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        previous = None

        for rectangle in rectangles:
            if not previous is None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                time.sleep(1)  # Adjust the sleep time to ensure content loads properly
            previous = rectangle

        return total_height, total_width
    """
    def scroll_down(self, driver):
    # Start with an initial guess for the total height
        total_height = 1000  # You can adjust this initial value as needed

        while True:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for a moment to let the content load
            time.sleep(2)  # Adjust the sleep time as needed

            # Get the new total height
            new_total_height = driver.execute_script("return document.body.scrollHeight")

            # If the new height is the same as the old height, we've reached the bottom
            if new_total_height == total_height:
                break

            total_height = new_total_height

        # Get the viewport width
        viewport_width = driver.execute_script("return window.innerWidth")

        return total_height, viewport_width


"""
# Example usage:
url = "https://www.falabella.com.co/falabella-co/product/34446468/Televisor-LG-65-Pulgadas-OLED-UHD-Smart-TV-OLED65C2/34446468?rid=Recs%21Home%21CO_F.com%21Rec_1%21x%21Populares%21home%2134446468%212%2118"  # Replace with the URL you want to capture
output_path = "results/webpage_screenshot.png"  # Replace with the desired output file path
screenshot_capture = WebpageScreenshotCapture(url, output_path)
screenshot_capture.capture_screenshot()
"""