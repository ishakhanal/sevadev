from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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

time.sleep(5)
SCROLL_PAUSE_TIME = 0.5
main_page = driver.current_window_handle

#Select category Dresses
driver.find_element_by_css_selector("#block_top_menu > ul > li:nth-child(2) > a").click()
time.sleep(5)

#scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#hovering mouse over required dress1
dress1 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[1]/div/a[1]/img")
hover1 = ActionChains(browser).move_to_element(dress1)

#adding dress1 to cart
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/div[2]/a[1]/span").click()
time.sleep(5)

#model poped up
for handle in driver.window_handles: 
    if handle != main_page: 
        popup = handle 

# change the control to popup page         
driver.switch_to.window(popup)

#continue shopping
driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/span/span").click()

#change window handler
driver.switch_to(main_page)

#hovering mouse over required dress2
dress2 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li[2]/div/div[1]/div/a[1]/img")
hover2 = ActionChains(browser).move_to_element(dress2)

#adding dress2 to cart
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li[2]/div/div[2]/div[2]/a[1]/span").click()
time.sleep(5)
# change the control to popup page         
driver.switch_to.window(popup)
#continue shopping
driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/span/span").click()
#change window handler
driver.switch_to(main_page)


#scroll up
driver.execute_script("window.scrollTo(0, -500)")
#Select Category T-SHIRTS 
driver.find_element_by_css_selector("#block_top_menu > ul > li.sfHoverForce > a").click()

#scroll down to select tshirt
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#hovering mouse over required tshirt
tshirt = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li[2]/div/div[1]/div/a[1]/img")
hover3 = ActionChains(browser).move_to_element(dress2)


#adding tshirt to cart
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/div[2]/a[1]/span").click()

#model poped up
for handle in driver.window_handles: 
    if handle != main_page: 
        popup2 = handle 

# change the control to popup page         
driver.switch_to.window(popup2)

#proceed to checkout
driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span").click()
time.sleep(10)

purchase_page = driver.current_window_handle
#opens purchase page
driver.switch_to(purchase_page)

#scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#click proceed to checkout
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span").click()

#scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)

#SIGn IN Form
driver.find_element_by_id("email").send_keys("ishakhanal25@gmail.com")
driver.find_element_by_id("passwd").send_keys("isha12345")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span").click()

#scroll bottom of page
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

#click on proceed to checkout
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/form/p/button/span").click()
time.sleep(10)

#agree to the terms and conditions
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div/p[2]/label").click()
#click proceed
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span").click()
time.sleep(5)

#scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(SCROLL_PAUSE_TIME)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#choose payment by bankwire
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[1]/div/p/a").click()
time.sleep(5)

#scroll bottom of the page
html.send_keys(Keys.END)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/form/p/button/span").click()
time.sleep(10)
driver.close()
