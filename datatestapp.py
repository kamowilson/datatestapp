from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost:3000/")
# Step 1. Firstname entry
element = driver.find_element_by_name("firstName")
element.send_keys("Kwame")
element.send_keys(Keys.RETURN)
# Step 2. Middle name entry
element = driver.find_element_by_name("middleName")
element.send_keys("Emmanuel")
# Step 3. Last name entry
element = driver.find_element_by_name("lastName")
element.send_keys("Wilson")
# Step 4. Phone number entry
element = driver.find_element_by_name("phoneNumber")
element.send_keys("1234567890")
# Step 5. Date Of Birth
element = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/main/div[3]/input')
element.send_keys("02/17/2021")
# Step 6. Address field
element = driver.find_element_by_name("address")
element.send_keys("Street Lion Hse.32,Accra - Ghana")
# Step 7. Adding User
element = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/a')
element.click()



