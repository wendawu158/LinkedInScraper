from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import credentials

# Setup the Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

username = credentials.username
password = credentials.password

try:
    # Define the URL
    url = "https://www.linkedin.com/search/results/companies/"

    # Opens the page
    print(f"Opening {url}...")
    driver.get(url)

    # Let the login page load
    time.sleep(2)

    driver.find_element("id", "username").send_keys(username)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("xpath", '//*[@id="organic-div"]/form/div[4]/button').click()

    # Let the search do its thing
    time.sleep(10)

    # Get the HTML
    html_content = driver.page_source
    print(f"Successfully retrieved {len(html_content)} characters of HTML.")

    # Saving it to a file
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        print("HTML saved to 'output.html'")

finally:
    # Close the browser
    driver.quit()
