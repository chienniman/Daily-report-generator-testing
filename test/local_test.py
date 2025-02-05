import time
import os
from common import setup_driver, upload_files, scroll_and_reset, upload_ppt

driver = setup_driver()
driver.get("http://127.0.0.1:5500/")
time.sleep(2)

current_dir = os.path.dirname(os.path.abspath(__file__))
upload_files(driver, current_dir)
scroll_and_reset(driver)
upload_ppt(driver, current_dir)

driver.quit()