from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Auto_login():
    def __init__(self, config):
        self.username = config["username"]
        self.password = config["password"]
        self.login_url = config["login_url"]
        self.driver = webdriver.Chrome()

    def login_config(self):
        username_field = self.driver.find_element(By.ID, 'username_tip')  # 根据实际情况替换选择器
        password_field = self.driver.find_element(By.ID, 'pwd_tip')  # 根据实际情况替换选择器

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

    def click_submit(self):
        submit_button = self.driver.find_element(By.ID, "loginLink")
        submit_button.click()
        response_code = 0
        return response_code

    def login(self):
        self.login_config()
        self.click_submit()
        time.sleep(3)

