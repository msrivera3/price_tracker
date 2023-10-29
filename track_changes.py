import pandas as pd
import build_report as br
from PIL import Image


def get_active_requests(path):
    requests = pd.read_csv("results/track_prices.csv")
    active = requests[requests["status"] == "ACTIVE"]
    return active

def get_current_price(req):
    # Capturing the full website screenshot
    url = input(req.Item_url)
    output_path = "results/testWebsite_SC.png"  
    screenshot_capture = WebpageScreenshotCapture(url, output_path)
    screenshot_capture.capture_screenshot()

    # Using the website screenshot to select the item price
    screenshot = Image.open(output_path)
    rectangle = tuple(req.rectangle.replace("(", "").replace(")","").split(","))
    selected_area = screenshot.crop(tuple)
    selected_area.save("results/cropped.png")

    # Using OCR to read the text on image
    price_path = "results/cropped.png"
    price_text = get_price(price_path)

    # FALTA CONSTUIR EL REPORTE USANDO LAS FUNCIONES DE BUILD_REPORT
    # DEJAMOS REGISTRO EN EL REPORTE SOLO SI EL PRECIO CAMBIA?
    # SI EL PRECIO CAMBIA DEJAMOS REGISTRO EN EL REPORTE DE TRACK_PRICES?

