from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import os

desired_caps = {
    "lt:options": {
        # "acceptInsecureCerts": True,
        # "acceptSslCerts": True,
        # "appiumVersion": "latest",
        #"app":"lt://APP10160591891685101090430535",
        "browserName": "Chrome",
        "build": "Goseetravel",
        "console": "False",
        "deviceName": "Galaxy S21 5G",
        # "appiumVersion": "1.22.0",
        # "enableNetworkThrottling": False,
        # "extendedDebuging": True,
        # "goog:chromeOptions": {
        #     "androidKeepAppDataDir": True,
        #     "args": [
        # "--disable-translate",
        # "--disable-features=Translate",
        # "--auto-accept-camera-and-microphone-capture",
        # "--use-fake-device-for-media-stream"
        #     ]
        # },
        # "headless": False,
        # "idleTimeout": "120",
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
    # el = driver.find_element("xpath",'/html/body/div[4]/div[2]/div/table[4]')
    # driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
    window_size = driver.get_window_size()

    # Define the start and end coordinates for the scroll action
    start_x = int(window_size['width'] / 2)
    start_y = int(window_size['height'] * 0.8)
    end_x = start_x
    end_y = int(window_size['height'] * 0.2)

    # Perform the scroll action
    i=0
    while(i<=5):
        driver.swipe(start_x, start_y, end_x, end_y, duration=50)
        i+=1
    # scroll_and_click_element(driver, "September 2023")

    # scrollable = MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
    # element_to_scroll_to = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("September 2023").instance(0)'

    # scrollable_element = driver.find_element(*scrollable)
    # element = driver.find_element(*element_to_scroll_to)

    # driver.scroll(scrollable_element, element)

    # date_click_01 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
    #     (MobileBy.XPATH, "//html/body/div[9]/div[2]/div[1]/div[2]/ul[2]/li[3]")))
    # date_click_01.click()

    # return_click = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
    #     (MobileBy.XPATH, "/html/body/div[8]/div[5]/div/div[3]/div[11]/div/div/div")))
    # return_click.click()

    # return_click_01 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
    #     (MobileBy.XPATH, "/html/body/div[9]/div[2]/div[1]/div[2]/ul[3]/li[1]")))
    # date_click_01.click()

    time.sleep(10)
    driver.quit()
startingTest()
