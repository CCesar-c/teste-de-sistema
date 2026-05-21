from selenium import webdriver
from selenium.webdriver.common.by import By
import time;

navegador = webdriver.Chrome()

try:
    navegador.get("https://banco-fake.netlify.app/")
    time.sleep(1)
    navegador.maximize_window()
    navegador.find_element(By.ID, 'inputRegisterName').send_keys("cesar")
    navegador.find_element(By.ID, 'inputRegisterEmail').send_keys("cesar@gmail.com")
    navegador.find_element(By.ID, 'inputRegisterPassword').send_keys("cesar123@")
    time.sleep(1)
    navegador.find_element(By.CLASS_NAME, "btnPrimary").click()
    time.sleep(1)
    navegador.find_element(By.CLASS_NAME, "btnSecondary").click()
    time.sleep(1)
    navegador.find_element(By.ID, 'inputLoginEmail').send_keys("cesar@gmail.com")
    navegador.find_element(By.ID, 'inputLoginPassword').send_keys("cesar123@")
    time.sleep(1)
    navegador.find_element(By.ID, "btnLogin").click()
    time.sleep(1)
    navegador.find_element(By.ID, "tabDepositar").click()
    navegador.find_element(By.ID, "inputDeposito").send_keys("1000")
    navegador.find_element(By.ID, "btnDepositar").click()
    time.sleep(1)
    navegador.find_element(By.ID, "tabSacar").click()
    time.sleep(1)
    navegador.find_element(By.ID, "inputSaque").send_keys("500")
    time.sleep(1)
    navegador.find_element(By.ID, "btnSacar").click()
    time.sleep(1)
    navegador.find_element(By.ID, "tabSaldo").click()
    time.sleep(1)
    navegador.find_element(By.ID, "tabLogout").click()
except ValueError:
    print(ValueError)


time.sleep(100)