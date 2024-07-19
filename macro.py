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

# 초단위 반환
def get_sec(time_str, time_format, is_server):
    sec = datetime.strptime(time_str, time_format)
    if is_server == 1:
        sec += timedelta(hours=9)
    return float(sec.timestamp())

target_sec = get_sec(apply_day_str, time_format, 0)

# 서버 시간
def get_server_time():
    response = urllib.request.urlopen(url)
    date_str = response.headers['Date']
    date_str = date_str.rstrip(' GMT')[5:]
    server_sec = get_sec(date_str, '%d %b %Y %H:%M:%S', 1)
    response.close()
    
    return server_sec

# 40초 전에 로그인
login_time = target_sec - 40                                  
while True:
    login_sec = get_server_time()

    if(login_time <= login_sec):
        driver.get(url)
        driver.find_element(By.ID, "userID").send_keys("**********")   # 아이디 삽입
        driver.find_element(By.ID, "userPW").send_keys("**********") # 비밀번호 삽입
        driver.find_element(By.ID, "btnLogin").click()
        break