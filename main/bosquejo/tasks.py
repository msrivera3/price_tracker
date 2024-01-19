from celery import shared_task
from screen.Engine.OCR import OCR
from screen.Engine.Screen import ScreenShot
from screen.Services.Email.SMTP_con import SmptConfig
from screen.Services.Auto_validate import Validate
from screen.Services.Console_info import Console

@shared_task
def prueba():


    validate = Validate()
    email = SmptConfig() 
 
    prices =  validate.aut_validate()
    
    print(prices)
    if prices["current_price"] != prices["db_price"]:
        
        price = prices["current_price"]
        o_price = prices["db_price"]
        email.notify("camiloandres_kane@hotmail.com","prueba", f"El precio cambio a {price}, precio inicial : {o_price}")
    else:
        
        Console.warning("El precio no ha cambiado!")