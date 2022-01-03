import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

book_button = browser.find_element_by_tag_name("button").click()

# решаем математический пример
x = browser.find_element_by_id("input_value").text
puzzle = math.log(abs(12 * math.sin(int(x))))

enterAnswer = browser.find_element_by_tag_name("input").send_keys(str(puzzle))

button = browser.find_element_by_id("solve").click()

#time.sleep(1)
#browser.quit()
