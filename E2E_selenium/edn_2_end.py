from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service("C:\\Users\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()

driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.find_element(By.ID, "btn-make-appointment").click()

driver.find_element(By.ID, "txt-username").send_keys("John Doe")
driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
driver.find_element(By.ID, "btn-login").click()

dropdown_facility = Select(driver.find_element(By.ID, "combo_facility"))
dropdown_facility.select_by_visible_text("Hongkong CURA Healthcare Center")
driver.find_element(By.ID, "chk_hospotal_readmission").click()
driver.find_element(By.ID, "radio_program_medicaid").click()
driver.find_element(By.ID, "txt_visit_date").send_keys("03/01/2023")
driver.find_element(By.ID, "txt_comment").send_keys("Hello! Will visit you on the specified date!")
driver.find_element(By.ID, "btn-book-appointment").click()
message = driver.find_element(By.CSS_SELECTOR, "div[class='col-xs-12 text-center'] h2").text
print(message)
assert "Appointment Confirmation" == message
