#
#
#                CASO DE PRUEBA PE 16
#
#




# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestModulo4():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_modulo4(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(841, 1040)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.LINK_TEXT, "Register here").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("alejnunez@uade.edu.ar")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("ABC123%&@")
    self.driver.find_element(By.ID, "cpassword").click()
    self.driver.find_element(By.ID, "cpassword").send_keys("ABC123%&@")
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").send_keys("Alejandro")
    self.driver.find_element(By.NAME, "lastName").click()
    self.driver.find_element(By.NAME, "lastName").send_keys("Nuñez")
    self.driver.find_element(By.NAME, "address1").click()
    self.driver.find_element(By.NAME, "address1").send_keys("W Washington St.")
    self.driver.find_element(By.NAME, "address2").click()
    self.driver.find_element(By.NAME, "address2").send_keys("N Orange Ave")
    self.driver.find_element(By.NAME, "zipcode").click()
    self.driver.find_element(By.NAME, "zipcode").send_keys("32801")
    self.driver.find_element(By.NAME, "city").click()
    self.driver.find_element(By.NAME, "city").send_keys("Orlando")
    self.driver.find_element(By.NAME, "state").click()
    self.driver.find_element(By.NAME, "state").send_keys("Florida")
    self.driver.find_element(By.NAME, "country").click()
    self.driver.find_element(By.NAME, "country").send_keys("Estados Unidos")
    self.driver.find_element(By.NAME, "phone").click()
    self.driver.find_element(By.NAME, "phone").click()
    self.driver.find_element(By.NAME, "phone").send_keys("2267533089")
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(13) > input").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("alejnunez@uade.edu.ar")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("ABC123%&@")
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input").click()
    
    #Assert aparece el mail en el campo de mail
    user_name = self.driver.find_element(By.CLASS_NAME, "dropbtn").text
    assert 'Hello,\nAlejandro' in user_name
    
    
