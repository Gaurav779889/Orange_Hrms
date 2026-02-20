from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class PIM_Page_Class:

    menu_pim_xpath = "//span[text()='PIM']"
    btn_add_xpath = "//button[normalize-space()='Add']"
    upload_photo_xpath = "//input[@type='file']"

    first_name_xpath = "//input[@placeholder='First Name']"
    middle_name_xpath = "//input[@placeholder='Middle Name']"
    last_name_xpath = "//input[@placeholder='Last Name']"
    btn_save_xpath = "//button[normalize-space()='Save']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_PIM(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.menu_pim_xpath)))
        self.driver.find_element(By.XPATH, self.menu_pim_xpath).click()

    def Click_Add(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.btn_add_xpath)))
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

    def Upload_Photo(self, image_path):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.upload_photo_xpath)))
        self.driver.find_element(By.XPATH, self.upload_photo_xpath).send_keys(image_path)

    def Enter_FirstName(self, firstname):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.first_name_xpath)))
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(firstname)

    def Enter_MiddleName(self, middlename):
        self.driver.find_element(By.XPATH, self.middle_name_xpath).send_keys(middlename)

    def Enter_LastName(self, lastname):
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(lastname)


    def Click_Save(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.btn_save_xpath)))
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
