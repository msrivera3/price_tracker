import string
import pytesseract
from PIL import Image, ImageOps
from ..Services.Console_info import Console


class OCR:
    
    def __init__(self) -> None:
        
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        Console.info("Iniciando OCR")
        
        
    def convert(self, img_path):
        
        img =  Image.open(img_path)
        
        img_to_gray = img.convert("L")  
        img_to_binary = img_to_gray.point(lambda p: p > 128 and 255)
        img_to_binary.save("C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\temp\\binary.png")
        
        ## Configuracion de tesseract, lista blanca de caracteres a buscar y segmentacion de 1 linea    
        price = pytesseract.image_to_string(img_to_binary, config='--psm 6 -c tessedit_char_whitelist=0123456789')
        # print("BLANCO el precio es :" + price)
        Console.info(f"Imagen convertida a string directamente : {price}")
        
        if price == "":

            Console.warning("Error al convertir directamente")
            img =  Image.open(img_path)
            
            img_to_gray = img.convert("L")  
            img_invert = ImageOps.invert(img_to_gray)
            img_to_binary = img_invert.point(lambda p: p > 128 and 255)
            img_to_binary.save("C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\temp\\invert.png")      
            price = pytesseract.image_to_string(img_to_binary)
            # print("INVERTIDO el precio es :" + price)
            Console.info("Imagen convertida a string con inversion : {price}")
               
        return self._clean_string(price)
    
    def _clean_string(self, string : string):
        
        delete_chars = " .,$"
        clean_string = string
        for char in delete_chars:
            clean_string = clean_string.replace(char, '')
        
        prince_float = float(clean_string)
        
        return prince_float
                   