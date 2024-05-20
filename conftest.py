
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.fullscreen_window()
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options,
                                  service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
    yield driver
    driver.quit()
