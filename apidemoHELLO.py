# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9"
caps["appium:deviceName"] = "localhost:50640"
caps["appium:app"] = "C:\\Users\\vdi-student\\Downloads\\ApiDemos-debug.apk"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="App")
el1.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(404, 671)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(436, 337)
actions.w3c_actions.pointer_action.release()
actions.perform()

el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
el2.click()
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Invoke Search")
el3.click()
el4 = driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/txt_query_prefill")
el4.click()
el4.send_keys("Hello Jacob!")

driver.quit()

