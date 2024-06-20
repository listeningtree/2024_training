from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/s")
#在输入框中输入值
elem=driver.find_element(By.NAME,"wd")
elem.send_keys("好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好")
sleep(3)
e=driver.find_element(By.NAME,"wd")
print(e.text)
#点击百度一下
driver.find_element(By.ID,"su").click()
sleep(3)

sleep(100)
driver.quit()