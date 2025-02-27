from behave import * # Importation de Behave
from selenium import webdriver # Importation de Selenium / WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

 # Pseudo-contante :
DELAY = 5 # Temporisation (nb. secondes)

@given('Je suis sur la page DuckDuckGo')
def ouvrir_moteur_recherche(context):
    context.driver = webdriver.Chrome() # Navigateur ChromeDriver
    sleep(DELAY) # Temporisation
    # context.driver.maximize_window() # Plein fenêtre
    context.driver.get('https://duckduckgo.com/') # Naviguer à l'adresse web
    context.driver.implicitly_wait(DELAY) # Marquer une temporisation

@when('Je saisis "{search_text}" dans la barre de Recherche')
def saisir_mots_clefs(context, search_text):
    context.driver.find_element(By.NAME, 'q').send_keys(search_text)
    sleep(DELAY) # Temporisation

# Correspond au 'And' de Gherkin
@when('je valide la saisie avec la touche [Entrée]')
def cliquer_recherche(context):
    context.driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
    sleep(DELAY)

@then('Je vois des résultats contenant "{text_result}"')
def verifier_resultats(context, text_result):
    # Vérification du terme recherché dans le contenu web résultant
    assert text_result in context.driver.page_source
