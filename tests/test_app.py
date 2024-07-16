from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = webdriver.Chrome()

driver.set_page_load_timeout(5)

try:
    driver.get("http://google.com")
    sleep(5)
    print("Acessou com sucesso")
except TimeoutException:
    print("Falha ao acessar")
finally:
    driver.quit()
