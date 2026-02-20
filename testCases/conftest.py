import pytest

<<<<<<< HEAD
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")

=======

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")#scope defind the class
def driver_setup(request):
    browser = request.config.getoption("--browser")
>>>>>>> 0d90d321fa968defed606e43122b8377e9590444
    if browser == "chrome":
        print("Launching Chrome Browser")
        from selenium import webdriver
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
<<<<<<< HEAD
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })

        driver = webdriver.Chrome(options=chrome_options)

=======

            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False

        }
                                               )
        driver = webdriver.Chrome(options=chrome_options)


>>>>>>> 0d90d321fa968defed606e43122b8377e9590444
    elif browser == "firefox":
        print("Launching Firefox Browser")
        from selenium import webdriver
        driver = webdriver.Firefox()
<<<<<<< HEAD

=======
>>>>>>> 0d90d321fa968defed606e43122b8377e9590444
    elif browser == "edge":
        print("Launching Edge Browser")
        from selenium import webdriver
        driver = webdriver.Edge()
<<<<<<< HEAD

=======
>>>>>>> 0d90d321fa968defed606e43122b8377e9590444
    elif browser == "headless":
        print("Launching Headless Browser")
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
<<<<<<< HEAD

    else:
        print("Invalid Browser")
        driver = None

    driver.maximize_window()
    request.cls.driver = driver

    yield   # ✅ VERY IMPORTANT

    driver.quit()   # ✅ runs AFTER test completes
=======
    else:
        print("Invalid Browser")
        driver = None
    driver.maximize_window()
    request.cls.driver = driver # for attache this file compulsary hai
    yield driver #import comulary line in code
    driver.quit()









>>>>>>> 0d90d321fa968defed606e43122b8377e9590444
