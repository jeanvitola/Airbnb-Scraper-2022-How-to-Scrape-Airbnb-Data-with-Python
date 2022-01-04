 #---------------------------->1) Librerias y Módulos<-----------------------
 
from selenium import webdriver
import os
import constans  as const
import time
from bs4 import BeautifulSoup
import pandas as pd


# ---------------------------------->2) Listas <---------------------------------
title=[]
rating=[]
city=[]
href=[]
price=[]
tipe=[]
host=[]
rooms=[]
beds=[]
bathrooms=[]
days=[]
days_2=[]

#Set para colección de datos
collection=[]


#------------------------------->3)Creando clases y métodos<-------------------


class Airbnb(webdriver.Chrome):
    def __init__(self,driver_path=os.pathsep + r'C:\SeleniumDrivers', teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])    #Evitar adverntencias del desarrollo   
        super(Airbnb,self).__init__(options=options)
        self.implicitly_wait(10) # Espera hasta que se carguen los elementos
        self.maximize_window() # maximizar windows 
        
        
        
    def __exit__(self,exc_type,exc_value,exc_tb):
        if self.teardown:
            self.quit()

    #// Entrada de URL a través de el archivo "constants"
    def land_firts_page(self):
        self.get(const.BASE_URL)

    #// Entrada de la ubicación
    def ubication(self,place_to_go):
        ubication_element=self.find_element_by_id("bigsearch-query-location-input")
        ubication_element.clear() 
        ubication_element.send_keys(place_to_go) #place_to_go será el párametro del lugar que se pasará
        time.sleep(3)
        first_result=self.find_element_by_css_selector(  
            'div[data-index="1"]'
            )
        first_result.click()
    
    #//Selecionar check_in
    time.sleep(3) 
    def  select_date (self,check_in):
        check_in_element = self.find_element_by_css_selector(
            f'div[data-testid="datepicker-day-{check_in}"]')  #Formato de fecha 2021-11-28"
        time.sleep(2)
        check_in_element.click()

    
    #//---->seleccionar check_out
    time.sleep(2)
    def select_date_out(self,check_out):
        check_out_element = self.find_element_by_css_selector(
            f'div[data-testid="datepicker-day-{check_out}"]')  #Formato de fecha 2021-11-28"
        time.sleep(2)
        check_out_element.click()
        
        
    #---->//seleccionar el numero de personas,niños y mascotas
    def select_person(self,count):
        select_extra=self.find_element_by_xpath('//*[@id="search-tabpanel"]/div/div[5]/div[1]/div/div[2]')
        select_extra.click()
        time.sleep(2)
        increase_button_element=self.find_element_by_css_selector('button[data-testid="stepper-adults-increase-button"]')
        for i in range(count):
            increase_button_element.click()
                
    
    def children_element(self,count):
        increase_button_element=self.find_element_by_css_selector('button[data-testid="stepper-children-increase-button"]')
        for i in range(count):
            increase_button_element.click()
    
    
    def babys_element(self,count):
        increase_button_element=self.find_element_by_css_selector('button[data-testid="stepper-infants-increase-button"]')
        for i in range(count):
            increase_button_element.click()  
            
    
    def pets_element(self,count):
        increase_button_element=self.find_element_by_css_selector('button[data-testid="stepper-pets-increase-button"]')
        for i in range(count):
            increase_button_element.click()  
            
    

    def search_element(self):
        search_element_button= self.find_element_by_css_selector('button[class="_1mzhry13"]')
        search_element_button.click()


    #--------------> Cookie <---------------------#
    # def cookie(self):
    #     cookie_element=self.find_element_by_css_selector('div._160gnkxa')
    #     try:
    #         cookie_element.click()
    #     except:
    #         pass 

    def element_parser(self):
        for j in range(1,15):
            print("ejecutando sin problemas, espere mientras se cumple el scraping de la página")
            for i in range(1,20):
                element = self.find_element_by_xpath("(//div[@class='_gig1e7'])["+str(i)  +"]")
                element.click()
                time.sleep(2)
                # Hacemos foco sobre la nueva pestaña
                self.switch_to.window(self.window_handles[1])
                # --- Ahora estamos trabajando en la URL-secundaria
                time.sleep(4) 
                
                #----------------------Elementos de la página--------------------------
                # title
                try:
                    title_house=self.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[1]/span/h1')
                    title.append(title_house.text)
                except:
                    title.append(None)
                
                # Rating
                try:
                    rating_house=self.find_element_by_css_selector("span._1ne5r4rt")
                    rating.append(rating_house.text)
                except:
                    rating.append(None)

                # city
                try:

                    city_house=self.find_element_by_css_selector("span._pbq7fmm")
                    city.append(city_house.text)
                except:
                    city.append(None)

                # Url
                try:
                    href_house=self.current_url
                    href.append(href_house)
                except:
                    href.append(None)

                # price/night
                try:
                    price_house=self.find_element_by_xpath('//*[@id="site-content"]/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/span[1]')
                    price.append(price_house.text)
                except:
                    price.append(None)

                # tipe
                try:
                    type_house=self.find_element_by_css_selector("h2._14i3z6h")
                    tipe.append(type_house.text)
                except:
                    tipe.append(None)


                # host- titulo del anfitriòn
                try:
                    host_house=self.find_element_by_xpath('//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/ol/li[1]/span')
                    host.append(host_house.text)
                except:
                    host.append(None)

                # Rooms--Cuartos
                try:
                    rooms_house=self.find_element_by_xpath('//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/ol/li[2]/span[2]')
                    rooms.append(rooms_house.text)
                except:
                    rooms.append(rooms_house.text)


                # bathrooms --baños
                try:
                    beds_house=self.find_element_by_xpath('//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/ol/li[3]/span[2]')
                    beds.append(beds_house.text)
                except:
                    beds.append(beds_house.text)

                # beds --camas
                try:
                    bathrooms_houses=self.find_element_by_xpath('//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/ol/li[4]/span[2]')
                    bathrooms.append(bathrooms_houses.text)
                except:
                    bathrooms.append(None)


            
            #------------------> Foco de la página <-----------------------------   
            
                time.sleep(3)
                # Cerrar la nueva pestaña de URL-secundaria
                self.close()

                # Cambiar el foco, para volver a la URL-principal
                self.switch_to.window(self.window_handles[0])
                time.sleep(3) 
                
            try: 
                next_page=self.find_element_by_xpath('//a[@aria-label="Siguiente"]')
                self.execute_script("arguments[0].click();", next_page) 
            except:
                print("No se encuentran mas páginas")
                
        time.sleep(5)         
        a={"title":title,"host":host,"city":city,"price":price,"rating":rating,"rooms":rooms,"bathrooms":bathrooms,"beds":beds,"tipe":tipe,"href":href,"days":days}
        df = pd.DataFrame.from_dict(a, orient='index')
        df = df.transpose()
        print(df)
        df.to_excel("Airbnb.xlsx", index=False)       
            
    












