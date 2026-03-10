import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()

    elif browser.lower() == "safari":
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()