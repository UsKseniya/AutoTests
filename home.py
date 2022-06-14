# ДОБАВЛЕНИЕ КОММЕНТАРИЯ
import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0,100);")
book = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0  .woocommerce > ul > li > a:nth-child(1)")
book.click()
review = driver.find_element_by_css_selector('[href="#tab-reviews"]')
review.click()
rating = driver.find_element_by_class_name("star-5")
rating.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice Book!")
author = driver.find_element_by_id("author")
author.send_keys("Xenon")
email = driver.find_element_by_id("email")
email.send_keys("firstname-lastname@domain.com")
submit = driver.find_element_by_id("submit")
submit.click()
driver.quit()

