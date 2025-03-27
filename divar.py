from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# baraaaye download va modiriate Chrome Driver ke selenium estefade mikone azash
from webdriver_manager.chrome import ChromeDriverManager
# baraye kar ba zaman
import time
# export va import kardan data ha
import pandas as pd


def scrape_divar(search_query, output_file):
    # Set up Chrome options
    options = Options()
    options.add_argument('--start-maximized') ## Open Chrome in maximized mode
    #in mige be moror gar ke biya va shenasayi script haye automatic ro be hadaghal bereson ke yemoghe be ma gir nade ke in script mokharebe
    options.add_argument('--disable-blink-features=AutomationControlled')#Avoid detection as automation

    # Initialize the WebDriver
    # miyad va mige biya ba in option hayi ke goftam chrome ro install kon
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Open Divar
        driver.get("https://divar.ir/s/tehran")
        #braye inke aval load beshe bad kar scriptemon bere sarvaghtesh
        time.sleep(5)

        # Find the search box and enter the search query
        #ba estefade az in va module ui library selenium biya va input ro dar safhe peyda kon ke tosh ye chizi gharare type konim
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

        # ba estefade az senf_key on chizi ke mikhaym ro minivisim to text box
        search_box.send_keys(search_query)
        #inja ba estefade az in Keys.RETURN miyaym va enter mizinam
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        # Scroll and wait for ads to load
        last_height = driver.execute_script("return document.body.scrollHeight")
        ads = []

        while True:
            # Wait for new ads to load
            time.sleep(3) # Adjust this time as needed

            # Extract ads
            ad_elements = driver.find_elements(By.CLASS_NAME, "kt-post-card")
            for ad in ad_elements:
                try:
                    #esme class hayike dar source html page divar vojod dare
                    title = ad.find_element(By.CLASS_NAME, "kt-post-card__title").text
                    price = ad.find_element(By.CLASS_NAME, "kt-post-card__description").text
                    location = ad.find_element(By.CLASS_NAME, "kt-post-card__bottom-description").text
                    link = ad.find_element(By.TAG_NAME, "a").get_attribute("href")

                    ads.append({
                        'Title': title,
                        'Price': price,
                        'Location': location,
                        'Link': link
                    })
                except Exception as e:
                    print(f"Error extracting ad: {e}")

            # Scroll down to load more ads
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            # Check if we reached the bottom of the page
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Save the data to Excel
        if ads:
            df = pd.DataFrame(ads)#Convert list of dictionaries to a DataFrame
            df.to_excel(output_file, index=False)
            print(f"Data successfully saved to {output_file}")
        else:
            print("No data found to save.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


search_query = "206 سفید"
output_file = "divar_ads.xlsx"
scrape_divar(search_query, output_file)
