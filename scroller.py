from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import os

capability = {
	"platformName": "ios",
	"deviceName": "iPhone 12",
	"platformVersion": "14",
	"app": "*********",
	"isRealMobile": True,
    "w3c":True,
}

def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "*********"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "***************"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=capability, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")
        driver.find_element_by_accessibility_id("ios_touchable_wrapper").click()
        # driver.swipe(194,731,191,799,duration=60000)
        picker_wheel=driver.find_element_by_xpath("//XCUIElementTypePicker[@name='ios_picker']")
#         picker_wheel = driver.find_element_by_ios_class_chain("**/XCUIElementTypePickerWheel")

# # Determine the size and position of the picker wheel
        picker_wheel_rect = picker_wheel.rect
        picker_wheel_x = picker_wheel_rect['x']
        picker_wheel_y = picker_wheel_rect['y']
        picker_wheel_width = picker_wheel_rect['width']
        picker_wheel_height = picker_wheel_rect['height']

# Calculate the start and end coordinates for the scroll gesture
        start_x = picker_wheel_x + picker_wheel_width / 2
        start_y = picker_wheel_y + picker_wheel_height / 2
        end_x = start_x
        end_y = start_y - picker_wheel_height / 2  # Example: scroll 50% up

#     # Perform the scroll gesture
        action = TouchAction(driver)
        action.press(x=298, y=736).move_to(x=294, y=799).release().perform()
        time.sleep(20)
        action.tap(x=346, y=609).perform()
        driver.find_element_by_xpath("//XCUIElementTypeOther[@name='Continuar']").click()
        time.sleep(30)
        driver.find_element_by_xpath("//XCUIElementTypeTextField[@name='username-login']").send_keys("Ritam")
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Return']").click()
        driver.quit()
    except:
        driver.quit()
startingTest()
