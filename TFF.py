from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

driver_path = "C:\\Users\erencakir\Desktop\chromedriver.exe"

browser = webdriver.Chrome(driver_path)

browser.get("http://www.tff.org.tr/default.aspx?pageID=130")

# //*[@id="ctl00_MPane_m_130_696_ctnr_m_130_696_tabArama_Tab3"]/span/span
time.sleep(5)
klube_gore = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_tabArama_Tab3']/span/span")

klube_gore.click()
time.sleep(2)

klub_adi = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_txtKulupAdi']")
klub_adi.send_keys("fenerbahçe")
time.sleep(2)

# //*[@id="ctl00_MPane_m_130_696_ctnr_m_130_696_btnSearch2"]
ara = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_130_696_ctnr_m_130_696_btnSearch2']")
ara.click()
a = browser.page_source

soup = BeautifulSoup(a, "lxml")

oyuncular = soup.find("table", attrs={"class": "MasterTable_TFF_Contents"})
print(oyuncular)

time.sleep(15)

browser.quit()
