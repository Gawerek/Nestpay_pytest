import pytest
from selenium import webdriver as selenium_webdriver

@pytest.fixture(scope="module")
def webdriver(request, url):
    """Obsługa Selenium WebDriver.

    Inspirowane: https://stackoverflow.com/questions/48450594/selenium-timed-out-receiving-message-from-renderer
                 / https://stackoverflow.com/a/52340526
    """

    driver_options = selenium_webdriver.ChromeOptions()

    driver_options.add_argument("--enable-automation")
    driver_options.add_argument("--disable-browser-side-navigation")
    driver_options.add_argument("--disable-dev-shm-usage")
    driver_options.add_argument("--disable-gpu")
    # driver_options.add_argument("--disable-extensions")
    # driver_options.add_argument("--silent")
    driver_options.add_argument("--disable-infobars")
    driver_options.add_argument("--lang=pl")
    driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument("--windows-size=1920x1080")
    if not request.config.getoption("--no-headless"):
        driver_options.add_argument("--headless=chrome")
    # chrome_profile = selenium_webdriver.chrome()
    # chrome_profile.accept_untrusted_certs = True
    # chrome_profile.set_preference("browser.download.folderList", 2)
    # chrome_profile.set_preference("browser.download.manager.showWhenStarting", False)
    # chrome_profile.set_preference("browser.download.dir", temp_downloads_dir_path)
    # chrome_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
    # prefs = {"download.default_directory": temp_downloads_dir_path}
    # driver_options.add_experimental_option("prefs", prefs)

    # webdriver_path
    webdriver_path = request.config.getoption("--webdriver-path")
    if webdriver_path:
        driver = selenium_webdriver.Chrome(executable_path=webdriver_path, options=driver_options)
    else:
        driver = selenium_webdriver.Chrome(options=driver_options)
    # Ustawienie rozdzielczości potrzebne do trybu headless
    # Dodanie argumentu "--start-maximized" do driver_options nie wystarcza
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    driver.get(url)
    # driver.implicitly_wait(1)

    yield driver

    driver.close()
