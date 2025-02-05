import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = Options()
    options.chrome_executable_path = "chromedriver.exe"
    return webdriver.Chrome(options=options)

def upload_files(driver, current_dir):
    # upload monthStocks
    monthStocks_input = driver.find_element(By.ID, "monthStocks")
    monthStocks_input.send_keys(os.path.join(current_dir, "data/pxmart-data/dp1.csv"))
    time.sleep(2)

    # upload todaySells
    todaySells_input = driver.find_element(By.ID, "todaySells")
    todaySells_input.send_keys(os.path.join(current_dir, "data/pxmart-data/sal.csv"))
    time.sleep(2)

    # upload dailyKpi
    dailyKpi_input = driver.find_element(By.ID, "dailyKpi")
    dailyKpi_input.send_keys(os.path.join(current_dir, "data/pxmart-data/kpi.xlsx"))
    time.sleep(2)

    # click generateReport btn
    generate_report_button = driver.find_element(By.ID, "generateReport")
    generate_report_button.click()
    time.sleep(3)

def scroll_and_reset(driver):
    # scroll to bottom
    result_table = driver.find_element(By.ID, "resultTable")
    driver.execute_script("arguments[0].scrollIntoView(false);", result_table)
    time.sleep(3)

    # scroll to top
    driver.execute_script("arguments[0].scrollIntoView(true);", result_table)
    time.sleep(3)

    # click reset btn
    reset_button = driver.find_element(By.ID, "reset")
    reset_button.click()
    time.sleep(3)

def upload_ppt(driver, current_dir):
    # upload xlsx2ppt
    xlsx2ppt_input = driver.find_element(By.ID, "xlsx2ppt")
    xlsx2ppt_input.send_keys(os.path.join(current_dir, "data/pxmart-data/place.xlsx"))
    time.sleep(10)

    # scroll to bottom
    pptTableContainer = driver.find_element(By.ID, "pptTableContainer")
    driver.execute_script("arguments[0].scrollIntoView(false);", pptTableContainer)
    time.sleep(3)
