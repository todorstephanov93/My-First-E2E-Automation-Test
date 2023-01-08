from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from python_self_framework.utilities.base_class import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.get("https://katalon-demo-cura.herokuapp.com/")
        self.driver.find_element(By.ID, "btn-make-appointment").click()

        self.driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        self.driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        self.driver.find_element(By.ID, "btn-login").click()

        dropdown_facility = Select(self.driver.find_element(By.ID, "combo_facility"))
        dropdown_facility.select_by_visible_text("Hongkong CURA Healthcare Center")
        self.driver.find_element(By.ID, "chk_hospotal_readmission").click()
        self.driver.find_element(By.ID, "radio_program_medicaid").click()
        self.driver.find_element(By.ID, "txt_visit_date").send_keys("03/01/2023")
        self.driver.find_element(By.ID, "txt_comment").send_keys("Hello! Will visit you on the specified date!")
        self.driver.find_element(By.ID, "btn-book-appointment").click()
        message = self.driver.find_element(By.CSS_SELECTOR, "div[class='col-xs-12 text-center'] h2").text

        assert "Appointment Confirmation" == message
