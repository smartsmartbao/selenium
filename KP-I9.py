from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner
import unittest

class test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = 'http://10.119.169.8:8080/ifrs9/#/login'

    def test_1(self):
        driver=self.driver
        driver.get(self.url)
        driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div[1]/input').send_keys('11')
        driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/button').click()
    def test_add_category(self):
        driver=self.driver
        ele1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/aside/ul[1]/li[3]/div')))
        ele1.click()
        ele2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/aside/ul[1]/li[3]/ul/li[1]')))
        ele2.click()
        button=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="categoryForm"]/div[2]/div/div/button/span')))
        button.click()
        add=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//li[contains(text(),'新增')]")))
        add.click()
        cate_drop=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addCategoryForm"]/div[1]/div/div/div/input')))
        cate_drop.click()
        choice=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/body/div[2]/div[1]/div[1]/ul/li[1]')))
        choice.click()
        start_time=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/section/div/form/div[1]/div/div[1]/input')))
        start_time.send_keys('2018-08-14')
        end_time=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/section/div/form/div[1]/div/div[2]/input')))
        end_time.send_keys('2018-12-31')
        cate_drop.click()
        type=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/section/div/form/div[2]/div/div/label[2]/span[1]/span')))
        type.click()
        pro_type=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/section/div/form/div[4]/div/div/div/input')))
        pro_type.click()
        pro=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/body/div[5]/div[1]/div[1]/ul/li[3]/span')))
        pro.click()
        confirm=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="addCategoryForm"]/div[2]/div/button[1]/span')))
        confirm.click()
        tag=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/section/div[2]/div[3]/table/tbody/tr[1]/td[3]/div')))
        self.assertEqual(tag.text,'测试产品B')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__=='__main__':
    # unittest.main()
    path='result.html'
    suit=unittest.TestSuite()
    suit.addTest(test1('test_1'))
    suit.addTest(test1('test_add_category'))
    with open(path,'wb') as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='KP I9Report',description='通过情况')
        runner.run(suit)