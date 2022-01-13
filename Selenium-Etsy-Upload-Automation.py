from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

color = str(input("Name: "))

def click(css):
    driver.find_element_by_css_selector(css).click()

def fill(id,input):
    driver.find_element_by_id(id).send_keys(input)

def upload(id,file):
    driver.find_element_by_id(id).send_keys(file)

def select(xpath):
    driver.find_element_by_xpath(xpath).click()

def js(xpath):
    b = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", b)

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\you\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=Profile 1') #e.g. Profile 3
driver = webdriver.Chrome(executable_path=r'C:\Users\chromedriver.exe', chrome_options=options)


email = "name@gmail.com"
password = "password"
title = "TEST"
desc = "TEST"
tags = "TEST1,TEST2"
price = "26"



driver.get("https://www.etsy.com/your/shops/tools/listings/create")
try:
    fill("join_neu_email_field",email)
    fill("join_neu_password_field",password)
    click("#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button")
except:
    "ALREADY LOGGED IN"
title = "Printed 40pc " + color.capitalize() + " Collage Kit "+color.capitalize()+" Aesthetic 4x6"
tags = "collage kit,collage wall,collage photos," + color + "," + color + " art,beige and green,cream and green,collage kit canada,collage art,wall kit,collage aesthetic,mood board,tezza"
collage = "C:\\Users\\you\Documents" + color + ".png"
upload("listing-edit-image-upload",collage)
upload("listing-edit-image-upload",r"C:\Users\you\Documents\images\1.png")
upload("listing-edit-image-upload",r"C:\Users\you\Documents\images\3.png")
fill("title-input",title)
a = driver.find_element_by_id("taxonomy-search")
a.send_keys("collage")
sleep(3)
a.send_keys(Keys.RETURN)
select("/html/body/div[3]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[7]/div[5]/div/div/fieldset/div[2]/div/div[1]/div/div/div/select/optgroup/option[1]")
select("/html/body/div[3]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[7]/div[5]/div/div/fieldset/div[2]/div/div[2]/div/div/div/select/optgroup/option[1]")
select("/html/body/div[3]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[7]/div[5]/div/div/fieldset/div[2]/div/div[3]/div/div/div/select/optgroup[1]/option")
with open("collagedesc.txt") as file:
    fill("description-text-area-input",file.read())
fill("tags",tags)
click("#page-region > div > div > div.page-body > div > div > div > div.panel.p-xs-2.p-md-4.mb-xs-2.mb-md-3.mb-lg-4 > div:nth-child(30) > div > fieldset > div.col-sm-8.col-xl-9.col-tv-10 > div.col-group.col-flush > div.col-xs-10.col-md-9.col-xl-6 > div > div.input-group-btn > button")
fill("price_retail-input",price)
fill("quantity_retail-input","5")
js("/html/body/div[3]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[14]/div/div/div[1]/div/div/div/div[3]/div/div[1]/div[4]/div/div[1]/div/input")
sleep(5)
select("/html/body/div[3]/section/div/div[4]/div/div/div/div[3]/div/div[1]/div/div/div[2]/button[2]")