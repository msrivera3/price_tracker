import pytesseract
import logging
import os
import time
import tkinter as tk
import build_report as br
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image, ImageDraw, ImageTk
from tkinter import filedialog
from helper import get_price
from website_screenshot import WebpageScreenshotCapture
from capture_price import CapturePrice

def main():

    # Capturing the full website screenshot
    url = input("Website URL: ")
    output_path = "results/testWebsite_SC.png"  
    screenshot_capture = WebpageScreenshotCapture(url, output_path)
    screenshot_capture.capture_screenshot()

    # Using the website screenshot to select the item price
    editor = CapturePrice(output_path)
    editor.run()
    rectangle = editor.selection

    # Using OCR to read the text on image
    price_path = "results/price_test.png"
    price_text = get_price(price_path)

    # Generating report
    price = br.price_text_to_number(price_text)
    report_dict = br.build_dict(url, price, rectangle, 30)
    br.save_report("results/track_prices.csv", report_dict)


if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    main()