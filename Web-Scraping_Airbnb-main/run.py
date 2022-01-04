from airbnb import Airbnb
import time 




try: 
    with Airbnb() as bot:
        bot.land_firts_page()
        time.sleep(2)
        print("\n")
        print("|*****************************************|")
        print("|**|      Web Scraping Airbnb            |**|")
        print("|**|           By:Jeanvitola             |**|")
        print("|**************************************|**°")
        print("")
        print("Seleccione una de las siguientes opciones:");
        bot.ubication(input("¿Qué lugar le gustaria Saber para obtener los datos?  "))
        bot.select_date(check_in=input("Qué día  hace Check in ? Ejemplo: 2021-11-28  "))
        bot.select_date_out(check_out=input("Qué día  hace Check Out ? Ejemplo: 2021-12-28  "))
        bot.select_person(count=int(input("¿Cuantas personas Viajarán?  ")))
        bot.children_element(count=int(input("¿Cuantas niños Viajarán?  " )) )
        bot.babys_element(count=int(input(("¿Cuantas bebes Viajarán?  "  ))))
        bot.pets_element(count=int(input("¿Cuantas mascotas Viajarán?   ")))
        bot.search_element()
        time.sleep(10)
        bot.element_parser()
        print("ejecutando con éxito")
        
except Exception as e:
    if 'in PATH' in str(e):
        print(
            
            'Por favor agregue el  PATH a su Selenium Driver \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
    
    
    #limit adults= 16, children=5, babys=5, pets= 5
    # Para los registros tiene un limite cada uno de ellos
    