# Selenium WebDriver Python coding
from selenium import webdriver
from os import path
# Give the location of the browser driver (the executable path). In Python, r means a raw string.
PROJECT_ROOT = path.abspath(path.dirname(__file__))
DRIVER_BIN = path.join(PROJECT_ROOT, 'chromedriver')
exec_path = r"E:\Training\SeleniumPython\Downloads\geckodriver-v0.26.0-win32\geckodriver.exe"
URL = r"https://www.wikipedia.org/"
# English language URL: https://en.wikipedia.org/
# Japanese language URL: https://ja.wikipedia.org/
# French language URL: https://fr.wikipedia.org/

# Define a Python list of languages. 
languages = ["en", "ja", "fr"]
driver = webdriver.Chrome(executable_path=DRIVER_BIN)
driver.get(URL)
# Print the Selenium WebDriver window handle of the original browser window. 
print ("Window handle of the current window is", driver.current_window_handle)

for i in range(len(languages)):
    # Call Selenium WebDriver execute script method with Javascript to open another tab. 
    driver.execute_script("window.open()")
    # Call Selenium WebDriver switch to method.
    # Selenium WebDriver window handles index 0 is the original tab.
    # In the for loop, use indexes starting from 1.
    driver.switch_to.window(driver.window_handles[i+1])
    language_URL = r"https://" + languages[i] + ".wikipedia.org/"
    driver.get(language_URL)
    print (language_URL, driver.window_handles[i+1], driver.title, driver.current_url)