from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?hl=es-la&source=auth_switcher') 
        time.sleep(3)
        user = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        user.clear()
        password.clear()
        user.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like(self):
        bot = self.bot
        time.sleep(3)
        bot.find_element_by_class_name('bIiDR').click()
        for i in range(1,2): #aumentar en caso de queder dar likes a mas publicaciones 
            time.sleep(2)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            likes =  bot.find_elements_by_tag_name('article')
            print(likes)
            for like in likes:
                try:
                    bot.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click()
                    time.sleep(10)
                except Exception:
                    time.sleep(30)

ad = TwitterBot('user','pass')
ad.login()
ad.like()
