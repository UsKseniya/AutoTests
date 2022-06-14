# РЕГИСТРАЦИЯ АККАУНТА
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")
time.sleep(3)

my_account = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
my_account.click()
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("email@subdomain.domain.com")
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("@d92P@ssword2022")
reg = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row .woocommerce-Button.button")
reg.click()
driver.quit()

# ЛОГИН В СИСТЕМУ
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
logout = driver.find_element_by_css_selector("ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a")
logout_get_text = logout.text
assert logout_get_text == "Logout"
driver.quit()
