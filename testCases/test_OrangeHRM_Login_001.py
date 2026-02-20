import pytest
import allure

from Utilities.logger import Logger_class
from pageObjects.Login_Page import Login_Page_Class
<<<<<<< HEAD
from pageObjects.PIM_Page import PIM_Page_Class
import os
=======
>>>>>>> 0d90d321fa968defed606e43122b8377e9590444
from Utilities.readConfig import ReadConfig
@pytest.mark.usefixtures("driver_setup")
class  Test_OrangeHRM_Login_001:
    driver = None
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    login_url = ReadConfig.get_login_url()
    log = Logger_class.get_logger()

    @allure.title("Verify OrangeHRM Login Page URL")
    @allure.description("This test verifies the URL of the OrangeHRM login page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Navigate to OrangeHRM Login Page")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123", name="Issue 123")
    @allure.testcase("https://github.com/allure-framework/allure-python/issues/123", name="Test Case 123")
    @allure.feature("OrangeHRM Login")
    @allure.story("Verify Login Page URL")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_verify_url_001(self):
        self.log.info("Starting Test: Verify OrangeHRM Login Page URL")
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page Loaded")
        if self.driver.title == "OrangeHRM":
            self.log.info("OrangeHRM Login Page URL Verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_pass.png")
            self.log.info("Screenshot of Passed Test Saved")
            allure.attach.file("screenshots\\test_verify_url_pass.png", name="test_verify_url_pass", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.error("OrangeHRM Login Page URL Not Verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_fail.png")
            allure.attach.file("screenshots\\test_verify_url_fail.png", name="test_verify_url_fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("test_verify_url_001 test Completed")
        self.log.info("=============================================================")


    @allure.title("Verify OrangeHRM Login")
    @allure.description("This test verifies the login functionality of the OrangeHRM application")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Enter Username and Password and Click Login")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123", name="Issue 123")
    @allure.testcase("https://github.com/allure-framework/allure-python/issues/123", name="Test Case 123")
    @allure.feature("OrangeHRM Login")
    @allure.story("Verify Login Functionality")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_OrangeHRM_Login_002(self):
        self.log.info("Starting Test: Verify OrangeHRM Login Functionality")
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page Loaded")
        lp = Login_Page_Class(self.driver)
        self.log.info("Entering Username and Password")
        lp.Enter_Username(self.username)
        lp.Enter_Password(self.password)
        self.log.info("Clicking Login Button")
        lp.Click_Login()
        self.log.info("Login Attempt Completed")
        if lp.verify_login() == "Login Successful":
            self.log.info("Login Successful")
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_Login_002_pass.png")
            self.log.info("Screenshot of Passed Test Saved")
            allure.attach.file("screenshots\\test_OrangeHRM_Login_002_pass.png", name="test_OrangeHRM_Login_002_pass", attachment_type=allure.attachment_type.PNG)
            lp.Click_Menu()
            lp.Click_Logout()
            assert True
        else:
            self.log.error("Login Failed")
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_Login_002_fail.png")
            allure.attach.file("screenshots\\test_OrangeHRM_Login_002_fail.png", name="test_OrangeHRM_Login_002_fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("test_OrangeHRM_Login_002 test Completed")
        self.log.info("=============================================================")

<<<<<<< HEAD
    def test_Add_Employee_With_Photo_003(self):
        self.log.info("Starting Test: Add Employee With Profile Photo")

        self.driver.get(self.login_url)

        lp = Login_Page_Class(self.driver)
        lp.Enter_Username(self.username)
        lp.Enter_Password(self.password)
        lp.Click_Login()

        if lp.verify_login() == "Login Successful":

            pim = PIM_Page_Class(self.driver)

            self.log.info("Clicking on PIM")
            pim.Click_PIM()

            self.log.info("Clicking on Add")
            pim.Click_Add()

            self.log.info("Uploading Profile Photo")
            image_path = r"E:\Credence\orange 7feb\Test_Data\Profile.jpeg"
            pim.Upload_Photo(image_path)

            self.log.info("Entering Employee Details")
            pim.Enter_FirstName("Gaurav")
            pim.Enter_MiddleName("Sanjay")
            pim.Enter_LastName("Sakharkar")

            # ✅ Screenshot AFTER filling details BEFORE Save
            self.log.info("Taking Screenshot After Filling All Details")

            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            file_path = "screenshots\\filled_employee_details.png"
            self.driver.save_screenshot(file_path)

            allure.attach.file(
                file_path,
                name="filled_employee_details",
                attachment_type=allure.attachment_type.PNG
            )

            self.log.info("Clicking on Save")
            pim.Click_Save()

            self.log.info("Employee Added Successfully")
            lp.Click_Menu()
            lp.Click_Logout()

            assert True

        else:
            self.log.error("Login Failed - Cannot Add Employee")
            assert False

=======
>>>>>>> 0d90d321fa968defed606e43122b8377e9590444
# pytest -v -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser chrome