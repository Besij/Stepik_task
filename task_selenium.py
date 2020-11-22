import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '100')
)

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(int(x))

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button2 = browser.find_element_by_id("solve")
button2.click()

time.sleep(2)

browser.close()
