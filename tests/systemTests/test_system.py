import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestSystem(unittest.TestCase):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_routeToEasyGame(self):
        self.driver.get('https://chess-es2-20221.herokuapp.com/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .button-style").click()
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .button-style").click()
        self.assertEqual(self.driver.current_url, "https://chess-es2-20221.herokuapp.com/gamepage/easy")
    

    def test_routeToHardGame(self):
        self.driver.get('https://chess-es2-20221.herokuapp.com/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) h2").click()
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) h2").click()
        self.assertEqual(self.driver.current_url, "https://chess-es2-20221.herokuapp.com/gamepage/hard")


    def test_routeToLevels(self):
        self.driver.get('https://chess-es2-20221.herokuapp.com/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .button-style").click()
        self.assertEqual(self.driver.title, "Níveis do jogo")

    def test_routeToRules(self):
        self.driver.get('https://chess-es2-20221.herokuapp.com/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) h2").click()
        self.assertEqual(self.driver.title, "Regras do jogo")

    def test_routeToAbout(self):
        self.driver.get('https://chess-es2-20221.herokuapp.com/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(3) > .button-style").click()
        self.assertEqual(self.driver.title, "Sobre o jogo")

    def test_routeToIaFight(self):
        self.driver.get('https://chess-es2-20221.herokuapp.com/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4) h2").click()
        self.assertEqual(self.driver.current_url, "https://chess-es2-20221.herokuapp.com/ia_fight/")

    def test_backToMenuFromEasyGame(self):
        self.driver.get('https://chess-es2-20221.herokuapp.com/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) h2").click()
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) h2").click()
        self.driver.find_element(By.CSS_SELECTOR, "img").click()
        self.assertEqual(self.driver.current_url, "https://chess-es2-20221.herokuapp.com/")

    def test_backToMenuFromHardGame(self):
        self.driver.get('https://chess-es2-20221.herokuapp.com/')
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) h2").click()
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) h2").click()
        self.driver.find_element(By.CSS_SELECTOR, "img").click()
        self.assertEqual(self.driver.current_url, "https://chess-es2-20221.herokuapp.com/")



if __name__ == '__main__':
    unittest.main()