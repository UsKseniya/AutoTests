# ОТОБРАЖЕНИЕ СТРАНИЦЫ ТОВАРА
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
book = driver.find_element_by_css_selector(".post-181 > .woocommerce-LoopProduct-link")
book.click()
title = driver.find_element_by_css_selector("h1.product_title.entry-title")
title_get_text = title.text
assert title_get_text == "HTML5 Forms"
driver.quit()

#КОЛИЧЕСТВО ТОВАРОВ В КАТЕГОРИИ
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("UsKseniya@domain.com")
password = driver.find_element_by_id("password")
password.send_keys("@d92P@ssword2022")
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
category = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]')
category.click()
count = driver.find_elements_by_class_name("product")
if len(count) == 3:
    print("Число товаров = 3")
else:
    print("Ошибка")
driver.quit()

#СОРТИРОВКА ТОВАРОВ
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("UsKseniya@domain.com")
password = driver.find_element_by_id("password")
password.send_keys("@d92P@ssword2022")
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
from selenium.webdriver.support.select import Select
items_selector = driver.find_element_by_name("orderby")
items_selector_default = items_selector.get_attribute("value")
if items_selector_default == "menu_order":
    print("Выбрана сортировка по умолчанию")
else:
    print("Выбрана сортировка НЕ по умолчанию")
sort_by_price = driver.find_element_by_css_selector("select.orderby")
select = Select(sort_by_price)
select.select_by_value("price-desc")
sort_by_price = driver.find_element_by_css_selector("select.orderby")
sort_by_price_selected = sort_by_price.get_attribute("value")
if sort_by_price_selected == "price-desc":
    print("Сортировка по цене от большего к меньшему")
else:
    print("Ошибка")
driver.quit()

# ОТОБРАЖЕНИЕ, СКИДКА ТОВАРА
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("UsKseniya@domain.com")
password = driver.find_element_by_id("password")
password.send_keys("@d92P@ssword2022")
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
android_book = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product/android-quick-start-guide/"]')
android_book.click()

old_price = driver.find_element_by_css_selector("del>.woocommerce-Price-amount.amount")
old_price_text = old_price.text
assert old_price_text == "₹600.00"
new_price = driver.find_element_by_css_selector(" div:nth-child(2) > p > ins > span")
new_price_text = new_price.text
assert new_price_text == "₹450.00"
img = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-main-image.zoom")))
img.click()
close = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
close.click()
driver.quit()

#ПРОВЕРКА ЦЕНЫ В КОРЗИНЕ
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
add = driver.find_element_by_css_selector(".post-182.product-type-simple  a.button.product_type_simple")
add.click()
time.sleep(3)
item = driver.find_element_by_class_name("cartcontents")
item_get_text = item.text
assert item_get_text == "1 Item"
price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
price_get_text = price.text
assert price_get_text == "₹180.00"
basket = driver.find_element_by_class_name("wpmenucart-contents")
basket.click()
subtotal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount.amount")))
print(subtotal.text)
total = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount")))
print(total.text)
driver.quit()

# РАБОТА В КОРЗИНЕ
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
driver.execute_script("window.scrollBy(0,300);")
book1 = driver.find_element_by_css_selector(".post-182.product-type-simple  a.button.product_type_simple")
book1.click()
time.sleep(3)
book2 = driver.find_element_by_css_selector(".post-180 a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
book2.click()
basket = driver.find_element_by_class_name("wpmenucart-contents")
basket.click()
time.sleep(3)
remove = driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td.product-remove > a")
remove.click()
undo = driver.find_element_by_css_selector('.woocommerce-message >a')
undo.click()
quan = driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td.product-quantity > div > input")
quan.clear()
quan.send_keys(3)
update = driver.find_element_by_css_selector("tbody > tr:nth-child(3) > td > input.button")
update.click()
quan_check = quan.get_attribute('value')
assert quan_check == "3"
time.sleep(3)
coupon = driver.find_element_by_css_selector("tr:nth-child(3) > td > div > input.button")
coupon.click()
time.sleep(3)
attention = driver.find_element_by_css_selector(".woocommerce-error > li")
attention_text = attention.text
if attention_text == "Please enter a coupon code.":
    print('Text - "Please enter a coupon code."')
else:
    print("ERROR")
driver.quit()

# ПОКУПКА ТОВАРА
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
driver.execute_script("window.scrollBy(0,300);")
book = driver.find_element_by_css_selector(".post-182.product-type-simple  a.button.product_type_simple")
book.click()
time.sleep(3)
basket = driver.find_element_by_class_name("wpmenucart-contents")
basket.click()
time.sleep(3)
checkout = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
checkout.click()
first_name = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.ID, "billing_first_name")))
first_name.send_keys("Kseniya")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Usoltseva")
email = driver.find_element_by_id("billing_email")
email.send_keys("UsKseniya@domain.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("+79234147958")
country = driver.find_element_by_id("s2id_billing_country")
country.click()
search = driver.find_element_by_id("s2id_autogen1_search")
search.send_keys("Russia")
choice = driver.find_element_by_class_name("select2-match")
choice.click()
street = driver.find_element_by_css_selector("input#billing_address_1")
street.send_keys("Nekrasova")
city = driver.find_element_by_css_selector("#billing_city.input-text")
city.send_keys("Novosibirsk")
state = driver.find_element_by_css_selector("input#billing_state")
state.send_keys("Novosibirsk")
postcode = driver.find_element_by_css_selector("input#billing_postcode")
postcode.send_keys("630005")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
payment = driver.find_element_by_id("payment_method_cheque")
payment.click()
order = driver.find_element_by_id("place_order")
order.click()
thanks = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-thankyou-order-received")))
thanks_text = thanks.text
assert thanks_text == "Thank you. Your order has been received."
method = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td")))
method_text = method.text
assert method_text == "Check Payments"
driver.quit()
