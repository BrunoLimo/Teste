from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep
import pytest
import subprocess

#Código que será chamado para todos os testes
@pytest.fixture
def driver():
    process = subprocess.Popen(['python','-m', 'streamlit','run','src/app.py'])
    
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(5)
    yield driver
    
    driver.quit()
    process.kill()
    
def test_app_opens(driver):
    driver.get("http://localhost:8501")
    sleep(5)
