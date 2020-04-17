#!/usr/bin/python3

import unittest
from selenium import webdriver
import time
import os
import sys

try:
    if sys.argv[1].lower() == "chrome":
        driver = webdriver.Chrome(executable_path=os.getcwd()+'/drivers/chromedriver')
    elif sys.argv[1].lower() == "firefox":
        driver = webdriver.Firefox(executable_path=os.getcwd()+'/drivers/geckodriver')
except:
    raise Exception("Não é um navegador válido!")

wrongAnswer = os.getcwd()+"/desafio1.py"
correctAnswer = os.getcwd()+"/desafio2.py"

driver.get("http://admin:admin@127.0.0.1:8080/")

#Correct Answer

driver.find_element_by_id("resposta").send_keys(correctAnswer)
driver.find_element_by_css_selector(".btn-primary").click()
time.sleep(2)
table = driver.find_element_by_class_name("table")
tableRows = table.find_elements_by_tag_name("tr")
tableColumns = tableRows[1].find_elements_by_tag_name("td") 
assert "OK!" in tableColumns[2].text
print("Feedback: ",tableColumns[1].text)

time.sleep(2)

#Wrong Answer

driver.find_element_by_id("resposta").send_keys(wrongAnswer)
driver.find_element_by_css_selector(".btn-primary").click()
time.sleep(2)
table = driver.find_element_by_class_name("table")
tableRows = table.find_elements_by_tag_name("tr")
tableColumns = tableRows[1].find_elements_by_tag_name("td") 
assert "Erro" in tableColumns[2].text
print("Feedback: ",tableColumns[1].text)

time.sleep(2)
        

driver.close()