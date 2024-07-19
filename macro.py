from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time
import urllib.request
from datetime import datetime
from datetime import timedelta

#Chrome 옵션 설정
webdriver_options = webdriver.ChromeOptions()
webdriver_options.add_experimental_option("detach", True)  # 창을 닫지 않도록 설정

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=webdriver_options)
driver.implicitly_wait(15)
url = 'https://sugang.pusan.ac.kr/main'

# 수강신청 날짜
time_format = '%Y. %m. %d %H:%M:%S'
apply_day_str = '2024. 07. 20 01:32:00' # 희망과목담기 2024. 08. 06 10:00:00
