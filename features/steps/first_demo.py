from selenium import webdriver
from behave import *



@given('Je suis sur la page DuckDuckGo')
def ouvrir_moteur_recherche(context):
    context.driver = webdrive.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

