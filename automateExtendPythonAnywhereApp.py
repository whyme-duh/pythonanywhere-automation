import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import ast


def renew_pythonanywhere(USERNAME, PASSWORD):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--start-maximized")
    
    print("Initializing browser...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 15)
    
    try:
        driver.get("https://www.pythonanywhere.com/login/")
        
        wait.until(EC.presence_of_element_located((By.ID, "id_auth-username"))).send_keys(USERNAME)
        driver.find_element(By.ID, "id_auth-password").send_keys(PASSWORD)
        driver.find_element(By.ID, "id_next").click()
        
        wait.until(EC.url_changes("https://www.pythonanywhere.com/login/"))
        print("Successfully logged in.")
        
        web_tab_url = f"https://www.pythonanywhere.com/user/{USERNAME}/webapps/"
        driver.get(web_tab_url)
        
        extend_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Run until 1 month from today']")))
        
        extend_button.click()
        
        time.sleep(3)
        
    except Exception as e:
        print(f"❌ An error occurred during automation: {e}")
        driver.save_screenshot("error_screenshot.png")
        
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    USERNAME = ast.literal_eval(os.getenv("PA_USERNAME", "YOUR_USERNAME"))
    PASSWORD = os.getenv("PA_PASSWORD", "YOUR_PASSWORD")

    for username in USERNAME:
        renew_pythonanywhere(username, PASSWORD)
    print("All accounts are not extended!")
