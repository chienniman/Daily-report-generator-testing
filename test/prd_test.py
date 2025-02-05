import time
import os
from common import setup_driver, upload_files, scroll_and_reset, upload_ppt

driver = setup_driver()
driver.get("https://www.boris.idv.tw/Daily-report-generator/")
time.sleep(2)

current_dir = os.path.dirname(os.path.abspath(__file__))
upload_files(driver, current_dir)
scroll_and_reset(driver)
upload_ppt(driver, current_dir)

driver.quit()