# Finding the elements:
# by name,
# by id (fastest if the element id is unique)
# by class name,
# by link text, by partial link text

# by xpath (customizable, flexible, element hierarchy can be used better)
# by css selector (customizable, flexible)

# Functions from selenium
# find_element_by_id(id)

# 1. start the browser
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
# implicit wait is defined once when you start the browser and this will apply all find element steps

# 2. open the website, and click on 'No, thanks!' button
url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
driver.get(url)
# time.sleep(10) # one way of holding the execution and to wait for something
print("now clicking the 'No thanks' button..")
driver.find_element_by_link_text('No, thanks!').click()     # or down below
#some_button = driver.find_element_by_link_text('No, thanks!')
#some_button.click()

# 3. find the "Enter a" input box
#  find the "Enter b" input box
# enter the "20" text in a
# enter the "30" text in b
driver.find_element_by_id("sum1").send_keys("20")
bvalue_input = driver.find_element_by_id("sum2")
bvalue_input.send_keys("30")


# 4. find the "Get Total" button and click on that button
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sum_button = driver.find_element_by_xpath("//button[text()='Get Total']")
# sum_button = driver.find_element_by_link_text("Get Total")
# driver.execute_script("arguments[0].scrollIntoView();", sum_button)
sum_button.click()
# driver.close()  # close the current tab
# driver.quit()  # closes the browser
print("Steps are completed!")
