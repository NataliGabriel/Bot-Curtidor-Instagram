from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

perfil = input("perfil que deseja curtir: ")


class InstagramCurtidasBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"C:\\Users\\Spart\\AppData\\Local\\Programs\\Python\\Python39\\geckodriver.exe"
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('logando...')
            pass
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()

        user_element.send_keys(self.username)

        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)

        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))
        self.curtir_fotos(

        ) 


    def curtir_fotos(self):
        driver = self.driver
        driver.get('https://www.instagram.com/' + perfil + "/")
        time.sleep(5)
        for i in range(
                1, 2
        ): 
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(perfil + " fotos: " + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("pulando link inválido")
                continue
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("//span[@class='fr66n']").click()
                time.sleep(3)
            except Exception as e:
                print(e)
                time.sleep(5)


BotNataliJr = InstagramCurtidasBot(
    "usuario", "senha"
)  # Entre com o usuário e senha aqui
BotNataliJr.login()