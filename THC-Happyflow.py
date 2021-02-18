from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://thc-testapp.netlify.app/")

# Step 1. Test for firstname scenario
firstname_element = browser.find_element_by_name("firstName")
firstname_element.send_keys("Kwame")

# Step 2. Test for middle name scenario
middleName_element = browser.find_element_by_name("middleName")
middleName_element.send_keys("Emmanuel")

# Step 3. Test for last name scenario
lastName = browser.find_element_by_name("lastName")
lastName.send_keys("Wilson")

# Step 4. Test for phone number scenario
phoneNumber = browser.find_element_by_name("phoneNumber")
phoneNumber.send_keys("0201234567")

# Step 5. Test for date of Birth scenario
DOB = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/main/div[3]/input')
DOB.send_keys("02/17/2021")

# Step 6. Test for address field
address = browser.find_element_by_name("address")
address.send_keys("Street Ato Hse.32, Accra - Ghana")

# Step 7. Test for adding user
add_user = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/a')
add_user.click()



