import pytesseract
from PIL import Image



def get_price(image_path):
    # This function takes a price image as input and retrieves its content as text
    #inputs:
        # image_path: path to image of the item price
    #output:
        # extracted_text: string containing
    
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image, lang="eng")
    print(extracted_text)
    return extracted_text
