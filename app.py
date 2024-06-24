from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Chrome Webdriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--user-data-dir=./User_Data")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def send_message(phone_number, message, count):
    driver.get('https://web.whatsapp.com')

    input("Press Enter after scanning the QR code")

    for i in range(count):
        try:
            driver.get(f'https://web.whatsapp.com/send?phone={phone_number}')

            time.sleep(10)
            message_box = driver.find_element(By.XPATH, '//div[contains(@class, "_3Uu1_") and @contenteditable="true"]')
            message_box.send_keys(message)
            message_box.send_keys(Keys.RETURN)

            print(f"Message {i+1} sent to {phone_number}")
            time.sleep(0.5)

        except Exception as e:
            print(f"An error occured: {e}")


        driver.refresh()
        time.sleep(5)


if __name__ == "__main__":
    phone_numbers = [
        '+254721255235', '+254727654220', '+254724844963', '+254723432321', 
        '+254722521492', '+254702247669', '+254722450106', '+254704653738', 
        '+254721637584', '+254725933138', '+254722575196', '+254724111140', 
        '+254722896442', '+254722741731', '+254724662381', '+254722525011', 
        '+254722510046', '+254714110769', '+254723011199', '+254722756800', 
        '+254720203201', '+254722510756', '+254720845042', '+254717036457', 
        '+254722140765', '+254722788205', '+254725234097', '+254722764985', 
        '+254720451803', '+254722680522', '+254722896442', '+254722894565'
    ]

    message = "RejectFinanceBill2024"
    count = 5

    for phone_number in phone_numbers:
        send_message(phone_number, message, count)


    driver.quit()
