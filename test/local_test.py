import time
import os
from common import setup_driver, upload_files, scroll_and_reset, upload_ppt, click_store_button, click_download_excel_button

driver = setup_driver()
driver.get("http://127.0.0.1:5500/")
time.sleep(2)

current_dir = os.path.dirname(os.path.abspath(__file__))
upload_files(driver, current_dir)
click_store_button(driver)
click_download_excel_button(driver)
scroll_and_reset(driver)
upload_ppt(driver, current_dir)

driver.quit()