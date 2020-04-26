import selenium
from selenium import webdriver
import json



# Step -0 Get the input from the user
# dlnum = input("Enter the DL no.")
# dob = input("Enter date of birth as dd-mm-yyyy")
dlnum = "DL-0420110149646"
dob = "09-02-1976"

# Step -1 get the instance of the driver and reach the requested url
driver = webdriver.Chrome("F:\selenium-scraper\chromedriver.exe")  #Replace the path to web driver
driver.get("https://parivahan.gov.in/rcdlstatus/?pur_cd=101")
driver.implicitly_wait(10)

# Step -2 send data into the input boxes 
dl_num_input = driver.find_element_by_xpath('//*[@id="form_rcdl:tf_dlNO"]')
dl_num_input.send_keys(dlnum)
dob_input = driver.find_element_by_xpath('//*[@id="form_rcdl:tf_dob_input"]')
dob_input.send_keys(dob)
captcha = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt34:CaptchaID"]')
answer = input("Enter captcha = ") # captcha is handled manually
captcha.send_keys(answer)
# Step -3 Handle the captcha

# Step -4 Submit the details
try:
    driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt46"]').click()

except:
    driver.quit()

# Step -5 Scrape the details
status = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[1]/td[2]/span').text
name = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[2]/td[2]').text
doi = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[3]/td[2]').text
last_trans = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[4]/td[2]').text
doe = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[2]/tbody/tr[1]/td[3]').text
category = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt167_data"]/tr/td[1]').text
cov = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt167_data"]/tr/td[2]').text

data = {
    "status" : status,
    "holder name" : name,
    "date of issue" : doi,
    "date of expiry" : doe,
    "last transaction at" : last_trans,
    "category" : category,
    "vehicle class" : cov
}

data = json.dumps(data)
print(data)
# driver.quit()

