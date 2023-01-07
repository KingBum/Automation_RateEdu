import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://my.uda.edu.vn/sv/svlogin")

driver.find_element(By.NAME, "User").send_keys("52888")
driver.find_element(By.NAME, "Password").send_keys("abc.12345")
driver.find_element(By.ID, "Lnew1").click()

find_length = len(driver.find_elements(By.CLASS_NAME ,'btn-danger'))
print(find_length)
list_count = 0
while (list_count < find_length):

    driver.find_element(By.XPATH, "//*[@id='MainContent_GridView1']/tbody/tr[1]/td/div[1]/div/div/table/tbody/tr/td[2]/h4/a[2]").click()

    driver.switch_to.window(driver.window_handles[1])
    for x in range(3):
        driver.find_element(By.XPATH, f"//*[@id='MainContent_Gks_GV5_0_RPA4_{x}']/tbody/tr/td[4]/label").click()
    driver.find_element(By.ID, "MainContent_Gks_Lnext_0").click()
    time.sleep(1)


    for x in range(12):
        driver.find_element(By.XPATH, f"//*[@id='MainContent_Gks_GV5_1_RPA4_{x}']/tbody/tr/td[4]/label").click()
    driver.find_element(By.ID, "MainContent_Gks_Lnext_1").click()
    time.sleep(1)


    for x in range(3):
        driver.find_element(By.XPATH, f"//*[@id='MainContent_Gks_GV5_2_RPA4_{x}']/tbody/tr/td[4]/label").click()
    driver.find_element(By.XPATH, f"//*[@id='MainContent_Gks_GV5_2_RPA4_3']/tbody/tr/td[1]/label").click()
    driver.find_element(By.ID, "MainContent_Gks_Lsend_2").click()
    time.sleep(2)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    time.sleep(2)
