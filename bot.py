from os import path
from selenium import webdriver
from time import sleep


ID_NUMBER = "1710500259676"
NAME = "ณพกร"
SURNAME = "สุทธิจิตตานนท์"
CHASSIS_NUMBER = "mrhfe1680np100810"
MOBILE_NUM = "0810004833"
NUMBER = "9998"

# ID_NUMBER = "1413434852713"
# NAME = "เอ"
# SURNAME = "บี"
# CHASSIS_NUMBER = "aaaaaaaaaaaaaaaaa"
# MOBILE_NUM = "0811111111"
# NUMBER = "9998"

PROJECT_ROOT = path.abspath(path.dirname(__file__))
DRIVER_BIN = path.join(PROJECT_ROOT, 'chromedriver')

browser = webdriver.Chrome(executable_path = DRIVER_BIN)
browser.get('https://reserve.dlt.go.th/reserve/s.php')
j = 0

while j < 60:
    if j > 0:
        try:
            browser.switch_to.alert.accept()
            break
        except:
            browser.execute_script('window.open()')
            browser.switch_to.window(browser.window_handles[j])
            browser.get('https://reserve.dlt.go.th/reserve/s.php')
        
    j = j + 1

    try:
        browser.find_element_by_xpath('//input[@type="submit"]').click()

        browser.find_element_by_xpath('//input[@value="    รถกระบะ 4 ประตู / รถเก๋ง   "]').click()

        # browser.find_element_by_xpath('//td/input').send_keys(NAME)

        loop = browser.find_elements_by_xpath('//td')

        for span in loop:
            if span.text == 'เลขบัตรประชาชน/ทะเบียนการค้า/หนังสือเดินทาง':
                mark_text = 0
                break
            elif span.text == 'คำนำหน้าชื่อ':
                mark_text = 1
                break

        loop = browser.find_elements_by_xpath('//td/input')
        i = 0

        if mark_text == 0:
            for span in loop:
                if i == 0:
                    data = ID_NUMBER
                    span.send_keys(data)
                elif i == 1:
                    data = NAME
                    span.send_keys(data)
                elif i == 2:
                    data = SURNAME
                    span.send_keys(data)
                else:
                    break

                i = i + 1
        elif mark_text == 1:
            for span in loop:
                if i == 0:
                    data = NAME
                    span.send_keys(data)
                elif i == 1:
                    data = SURNAME
                    span.send_keys(data)
                elif i == 2:
                    data = ID_NUMBER
                    span.send_keys(data)
                else:
                    break

                i = i + 1

        # browser.find_element_by_xpath('//td[@colspan="2"]/input').send_keys(SURNAME)
        # browser.find_element_by_xpath('//td[@colspan="2"]/input[2]').send_keys(ID_NUMBER)
        browser.find_element_by_xpath('//option[@value="นาย"]').click()
        browser.find_element_by_xpath('//option[@value="HONDA"]').click()
        browser.find_element_by_xpath('//input[@onkeypress="check_number1()"]').send_keys(CHASSIS_NUMBER)
        browser.find_element_by_xpath('//input[@onkeypress="check_number()"]').send_keys(MOBILE_NUM)
        browser.find_element_by_xpath('//input[@id="number"]').send_keys(NUMBER)
        sleep(23)
        browser.find_element_by_xpath('//input[@type="submit"]').click()
        browser.switch_to.alert.accept()
        continue
    except:
        pass