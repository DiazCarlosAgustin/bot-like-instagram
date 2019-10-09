# librerias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class TwitterBot:
    def __init__(self, username, password,url):
        self.username = username
        self.password = password
        self.url = url
        # navegador usado
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        # url de login
        bot.get('https://www.instagram.com/accounts/login/?hl=es-la&source=auth_switcher') 
        time.sleep(3)
        # guardo el usuario
        user = bot.find_element_by_name('username')
        # guardo el password
        password = bot.find_element_by_name('password')
        # limpio los campos
        user.clear()
        password.clear()
        # ingreso el usuario y la clave
        user.send_keys(self.username)
        password.send_keys(self.password)
        # ingresar
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like(self):
        bot = self.bot
        time.sleep(3)
        bot.find_element_by_class_name('bIiDR').click()
        time.sleep(2)
        # url del usuario al que voy a dar like
        bot.get(self.url) 
        time.sleep(2)
        for e in range(1,20):
            time.sleep(1)
            # realiza un scroll
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            # guardo todos los post encontrados mientras hago el scroll
            posts = bot.find_elements_by_class_name('v1Nh3')
            # guardo en un array las url de cada foto en los posts
            links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]
            a = open("imgs.txt","w")
            for link in links:
                a.write(link + "\n")

            a.close()
        # #recorre todos los links que guardo en el paso anterior y va entrando a cada foto y da like 
        l = open("imgs.txt")
        linea = l.readline()
        while linea != "":
            link = linea
            bot.get(link)
            try:
                # hago click en el corazon para dar like a la foto
                bot.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click()
                time.sleep(10)
            except Exception:
                time.sleep(30)
            linea = l.readline()


user = input("Usuario: ")
contra = input("Contraseña: ")
url = input("URL del usuario: ")
ad = TwitterBot(user,contra,url)
ad.login()
ad.like()
