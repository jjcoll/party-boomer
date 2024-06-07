from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from urllib.parse import quote

def create_caos(url, song_name):
  # Example usage
  url += "/search?s="
  new_url = add_song_param(url, song_name)
  
  # Define headless options
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')  # Run in headless mode

  # Create Chrome WebDriver instance with headless options
  driver = webdriver.Chrome(options=options)

  print("Chrome Driver Version:", driver.service.process.args[0])
  driver.get(new_url)
  time.sleep(3)
  _button = driver.execute_script('return document.querySelector("body > app-shell").shadowRoot.querySelector("view-party").shadowRoot.querySelector("app-drawer-layout > div > iron-pages > party-search").shadowRoot.querySelector("party-track-search:nth-child(4)").shadowRoot.querySelector("div.icon-wrapper > paper-icon-button").shadowRoot.querySelector("#icon")')
  _button_selector = """
  document.querySelector("body > app-shell").shadowRoot.querySelector("view-party").shadowRoot.querySelector("app-drawer-layout > div > iron-pages > party-search").shadowRoot.querySelector("party-track-search:nth-child(4)").shadowRoot.querySelector("div.icon-wrapper > paper-icon-button").shadowRoot.querySelector("#icon")
  """

  # Use WebDriverWait to wait until the button is clickable
  wait = WebDriverWait(driver, 30)  # Adjust the timeout as needed
  # _button = wait.until(EC.element_to_be_clickable((By.XPATH, _button_selector)))
  driver.execute_script('arguments[0].click()', _button )
  driver.quit()


def add_song_param(url, song_name):
    # Encode the song name to make it URL safe
    encoded_song_name = quote(song_name)
    
    # Find the position of the existing 's=' parameter
    s_index = url.find('s=')
    
    # If 's=' is found in the URL, replace its value with the new song name
    if s_index != -1:
        # Find the end of the existing song name
        end_index = url.find('&', s_index)
        if end_index == -1:  # 's=' is the last parameter in the URL
            new_url = url[:s_index+2] + encoded_song_name
        else:
            new_url = url[:s_index+2] + encoded_song_name + url[end_index:]
    else:
        # If 's=' is not found, simply append it to the URL
        if '?' in url:
            new_url = url + '&s=' + encoded_song_name
        else:
            new_url = url + '?s=' + encoded_song_name
    
    return new_url


