from datetime import datetime
from win10toast import ToastNotifier
from selenium import webdriver


def check_bb_slots(mins):
        check=True
        toaster = ToastNotifier()
        while check:
            if datetime.now().minute % mins == 0:
                driver.find_element_by_id('checkout').click()
                check_text = ''
                while check_text != '':
                    check_text=driver.find_element_by_id('slotContent').text
                if "Please try again later" in check_text:
                    driver.find_element_by_class_name('slotmodal-btn-confirm').click()
                else:
                    toaster.show_toast("Big basket !","Slots are available!!!")
                    check=False
                    
                
bb_url='https://www.bigbasket.com/auth/login/'
basket_url='https://bigbasket.com/basket/?ver=1'
ch_dr="C:/Users/SS23388/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(ch_dr)                
driver.get(bb_url)
cont=input("Please Login and then press enter: ")
driver.get(basket_url)
check_bb_slots(15)