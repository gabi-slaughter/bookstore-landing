from bs4 import BeautifulSoup
# Need to use Selenium to read what JavaScript renders after page load
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Nightwing database URL being scraped
url = 'https://www.comics.org/character_name/4061/issues/'

# Creates instance of Chrome WebDriver, opens Chrome window
browser = webdriver.Chrome()
browser.get(url)
# Retrieves html source code after JavaScript render
html_source = browser.page_source
browser.quit()

# Send GET request to URL
soup = BeautifulSoup(html_source, 'html.parser')

# Find <a> tags with '/series/' in href
series_links = soup.find_all('a', href=lambda href: href and "/series/" in href)

# Extract and add text of <a> tag to titles list
titles = [link.text for link in series_links]

# Print series titles
for title in titles:
    print(title)
