from selenium import webdriver
from selenium.webdriver.common.by import By
import time;
navegador = webdriver.Chrome()
objetos = [
  { "nome": "lapiz", "categoria": "papelaria", "quantidade": 6, "preco": 5 },
  { "nome": "abacaxi", "categoria": "fruta", "quantidade": 3, "preco": 75 },
  { "nome": "mouse", "categoria": "periferico", "quantidade": 2, "preco": 5 },
  { "nome": "cama", "categoria": "casa", "quantidade": 10, "preco": 105 },
  { "nome": "teclado", "categoria": "periferico", "quantidade": 3, "preco": 125 },
  { "nome": "pc", "categoria": "Pc", "quantidade": 600, "preco": 1005 },
  { "nome": "tv", "categoria": "casa", "quantidade": 10, "preco": 20005 },
  { "nome": "coca-cola", "categoria": "refri", "quantidade": 620, "preco": 105 },
  { "nome": "mochila", "categoria": "uniforme", "quantidade": 12, "preco": 395 },
  { "nome": "casa", "categoria": "casa", "quantidade": 2, "preco": 100000 }
];

navegador.get("https://sistema-3-estoque.netlify.app/")
time.sleep(1)
navegador.maximize_window()
time.sleep(1)

for i in objetos:
    navegador.find_element(By.ID, "nome-produto").send_keys(i['nome'])
    navegador.find_element(By.ID, "categoria-produto").send_keys(i['categoria'])
    navegador.find_element(By.ID, "quantidade-produto").send_keys(i['quantidade'])
    navegador.find_element(By.ID, "preco-produto").send_keys(i['preco'])
    navegador.find_element(By.ID, "btn-cadastrar").click()
    print(i)
time.sleep(1)
navegador.save_screenshot("print3.png")
time.sleep(1000)