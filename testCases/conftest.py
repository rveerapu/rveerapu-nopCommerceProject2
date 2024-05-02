from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    driver.implicitly_wait(3)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

def pytest_html_report_title(report):
    report.title = "My very own title! - NOP Commerce"

def pytest_configure(config):
    config.stash[metadata_key]["Tester"] = "Ramani"


