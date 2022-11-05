import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome('D:\\Automation\\chromedriver.exe')


@when(u'le site est lancé')
def LancheWebSite(context):
    context.driver.get("https://dev.citoyens-tunisiens-solidaires.org/")


@then(u'Ouvrir le popup de connexion')
def OpenPopupLogin(context):
    context.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[3]/div["
                                          "1]/div[1]/div[1]/div[1]/a[1]").click()
    time.sleep(2.0)


@then(u'Remplir les champs avec un email "{Email}" et un mot de passe "{Password}"')
def FillForm(context, Email, Password):
    context.driver.find_element(By.XPATH, "//input[@id='username_or_email']").send_keys(Email)
    context.driver.find_element(By.XPATH, "//input[@id='login_password']").send_keys(Password)
    time.sleep(2.0)


@then(u'Clicker sur le boutton Se connecter')
def ClickonLogin(context):
    time.sleep(2.0)
    context.driver.find_element(By.XPATH, "//input[@name='submit']").click()
    time.sleep(7.0)


@then(u'User est connecté avec succès')
def step_impl(context):
    print("conection succful 1")


@then(u'Fermer le browser')
def CloseBrowser(context):
    print("conection succful 2")
