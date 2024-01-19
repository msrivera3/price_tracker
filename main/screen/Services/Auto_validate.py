from ..Engine.OCR import OCR
from ..Engine.Screen import ScreenShot
from ..models import ImageTrack
from PIL import Image

class Validate:
    
    ocr : OCR  
    
    def __init__(self):
        
        self.screen = ScreenShot()
        self.ocr = OCR()
        
    def aut_validate(self):
        
        db = ImageTrack.objects.all()
        img1 = ""
        for img in db:
            img1 = img
           
        self.screen.take_screen(url_= img1.url, action="validate")
    
        ruta_entrada = "C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\temp\\temp_validate.png"
        ruta_salida = "C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\temp\\fini.png"

        img_cut = Image.open("C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\temp\\temp_validate.png")
    
        x =  img.x
        y =  img.y 
        h =  img.height
        w = img.width
        
        img_cortada = img_cut.crop((x, y, x + w, y + h))
        img_cortada.save("C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\temp\\fini.png")
            
        price_found = self.ocr.convert(ruta_salida)    

        return  {"current_price" : price_found, "db_price" : img.price}