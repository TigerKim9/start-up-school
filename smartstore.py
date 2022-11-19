import pyperclip as pyperclip
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


def guide():
    print('[System]스마트스토어 판매봇에 오신 것을 환영합니다. <비즈매크로 : 비즈니스 자동화 서비스>')
    print('[System]스봇은 1인 비즈니스 업무 자동화를 위해 제작되었습니다.')
    print('[System]계정 정보나 데이터, 캐시를 일체 저장하지 않으며, 서버가 없는 프로그램입니다.')
    print('[System]전체 코드를 제공하는 학습 프로그램입니다.\n')
    print("[System]작업이 시작됩니다..*")


def login(driver):
    id = "네이버 아이디"
    pw = "네이버 비밀번호"
    driver.get("https://nid.naver.com/nidlogin.login")
    driver.implicitly_wait(10)
    clipboard_input(driver, 'id', id)
    clipboard_input(driver, 'pw', pw)
    xpath = """//*[@id="frmNIDLogin"]/fieldset/input"""
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)

def clipboard_input(driver, class_id, user_input):
    pyperclip.copy(user_input)
    driver.find_element_by_id(class_id).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)


def sendProduct(driver):
    check_btn = driver.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[1]')
    check_btn.click()
    consumer_id = driver.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[3]/div[4]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[9]/div').text
    print(consumer_id+'@naver.com')
    #send email()
    send_btn = driver.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[3]/div[5]/table/tbody/tr[2]/td/button[1]')
    send_btn.click()
    time.sleep(5)
    alert = Alert(driver)
    alert.accept()
    time.sleep(3)
    alert.accept()

def checkData(driver):
    driver.get('https://sell.smartstore.naver.com/#/naverpay/sale/delivery')
    driver.implicitly_wait(10)
    driver.switch_to.frame('__naverpay')
    check_btn = driver.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[2]/div[2]/button').click()
    time.sleep(2)
    exist = driver.find_element_by_class_name('tui-grid-layer-state').text
    if exist.find('데이터가 존재하지 않습니다') != -1 :
        print('현재 배송할 상품이 없습니다')
    else : 
        sendProduct(driver)
    time.sleep(100)

def __init__() :
    guide()
    driver = webdriver.Chrome(r'chromedriver.exe')
    login(driver)
    checkData(driver)

__init__()