# -*- coding:utf-8 -*-

#pip3 install selenium
from selenium import webdriver;

class taobao_infos:
    def __init__(self):
        url = r'https://login.taobao.com/member/login.jhtml';
        self.url = url;

        options = webdriver.ChromeOptions();
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        options.add_experimental_option('excludeSwitches', ['enable-automation']) 

        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options);
        self.wait = WebDriverWait(self.browser, 10)

    def login(self):
        self.browser.get(self.url);

        password_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login> .login-links > .forget-pwd')));

        password_login.click();

if __name__ == '__main__':
    chromedriver_path = "C:\\Users\\JimmySenny\\AppData\Local\\Programs\\Python\\Python37"

    a = taobao_infos();
    a.login();


