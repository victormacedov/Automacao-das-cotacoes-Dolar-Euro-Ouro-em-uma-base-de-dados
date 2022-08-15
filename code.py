from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Dólar
navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#Euro
navegador.get('https://www.google.com.br/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#Ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,em%20R%24%20292%2C87.')

cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')

navegador.quit()

import pandas as pd
tabela = pd.read_excel('Produtos.xlsx')
print(tabela)

# Atualizar as cotações

tabela.loc[tabela["Moeda"] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == 'Ouro', 'Cotação'] = float(cotacao_ouro)

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

# Exportação da tabela atualizada

tabela.to_excel('Produto Atualizados.xlsx', index='False')

# Nova base criada
tabela_nova = pd.read_excel("Produto Atualizados.xlsx")
print(tabela)
