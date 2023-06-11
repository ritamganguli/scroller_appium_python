from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import os

desired_caps = {
    "lt:options": {
        "browserName": "Chrome",
        "build": "Goseetravel",
        "console": "False",
        "deviceName": "Galaxy S21 5G",
        "isRealMobile": True,
        "name": "Date Range Picker issue",
        "platform": "android",
        "platformName": "android",
        "platformVersion": "12",
        "video": True,
        "visual": True,
        "w3c": True,
    },
}

def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "************"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "**************"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")
    driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")

    driver.get("https://www.airportrentals.com/")
    time.sleep(3)
    flight = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (MobileBy.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/form/div[3]/div[1]/div/div[4]/div[1]/div[1]/div/div[2]")))
    flight.click()
    window_size = driver.get_window_size()

    # Define the start and end coordinates for the scroll action
    start_x = int(window_size['width'] / 2)
    start_y = int(window_size['height'] * 0.8)
    end_x = start_x
    end_y = int(window_size['height'] * 0.2)

    # Perform the scroll action uptil where you want to scroll and also increase the duration accordingly
    i=0
    while(i<=5):
        driver.swipe(start_x, start_y, end_x, end_y, duration=50)
        i+=1

    time.sleep(10)
    driver.quit()
startingTest()
