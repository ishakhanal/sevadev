from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time 


#Opens Chromedriver in headlessmode
options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")


#Click SignIn button
time.sleep(5)

#scroll
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element_by_css_selector("#header > div.nav > div > div > nav > div.header_user_info > a").click()
time.sleep(10)

#Fill Email form
driver.find_element_by_id("email_create").send_keys('ishakhanal25@gmail.com')
driver.find_element_by_id("SubmitCreate").click()
time.sleep(5)


#Register Form
#Personal info
driver.find_element_by_css_selector("#account-creation_form > div:nth-child(1) > div.clearfix > div:nth-child(4) > label").click()
driver.find_element_by_name("customer_firstname").send_keys('Isha')
driver.find_element_by_name("customer_lastname").send_keys('Khanal')
driver.find_element_by_name("passwd").send_keys('isha12345')

#DateOfBirth
selectday = Select(driver.find_element_by_id('days'))
selectdays.select_by_value('3')
selectmonth = Select(driver.find_element_by_id('months'))
selectmonth.select_by_value('12')
selectyear = Select(driver.find_element_by_id('years'))
selectyear.select_by_value('1996')

#checkbox
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[7]/div/span/input").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[8]/div/span/input").click()
print("Personal Info Completed....")


#Address info
#scroll
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element_by_name("company").send_keys('sevadev')
driver.find_element_by_name("address1").send_keys('naagpokhari')
driver.find_element_by_name("address2").send_keys('societyBuilding')
driver.find_element_by_name("city").send_keys('Kathmandu')
#scroll
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#select state
selectstate = Select(driver.find_element_by_id('id_state'))
selectstate.select_by_value('14')
driver.find_element_by_name("postcode").send_keys('44600')
#select country
selectcountry = Select(driver.find_element_by_id('id_country'))
selectcountry.select_by_visible_text('United States')

driver.find_element_by_id("other").send_keys('Permanent address: Jhapa,Birtamode')
driver.find_element_by_id("phone").send_keys('023-542476')
driver.find_element_by_id("phone_mobile").send_keys('9862680074')
driver.find_element_by_id("alias").send_keys('Buddhanagar')
print("Address Info Completed....")

#Registerbutton
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[4]/button/span/text()").click()
time.sleep(5)
print("The form is submitted....")
driver.close()















