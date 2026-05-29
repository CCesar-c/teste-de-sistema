from selenium import webdriver
from selenium.webdriver.common.by import By
import time;

navegador = webdriver.Chrome()

navegador.get("https://sistema-4-urna.netlify.app/")
time.sleep(1)
navegador.maximize_window()
time.sleep(1)
child = navegador.find_elements(By.TAG_NAME, "button")
time.sleep(0.1)
# print(child[6].text)
child[1].click()
time.sleep(0.1)
child[2].click()
time.sleep(0.1)
navegador.find_element(By.CLASS_NAME, "btn-confirma").click()
time.sleep(0.1)
navegador.save_screenshot("print4.png")

# for i in child:
#     print(i.text)
#     if i.text == "6":
#         print(i.text)
#         if i.text == "7":
#             print(i.text)
#     else:
#         print("Nao e o butao que estou procurando")
# navegador.find_element(By.XPATH, "//button[contains(., '6')]").click()
# time.sleep(1)
# navegador.find_element(By.XPATH, "//button[contains('7')]").click()
# time.sleep(1)
# navegador.find_element(By.CLASS_NAME, "btn-confirma").click()
# time.sleep(1)
# navegador.save_screenshot("print4.png")
time.sleep(1000)