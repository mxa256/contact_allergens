import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from fuzzywuzzy import process

#Set up
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#Open the main allergen list page
URL = 'https://contactallergy.com/index.html'
driver.get(URL)
time.sleep(3)  # Give time for the page to load

#Scrape all allergen links
allergen_links = driver.find_elements(By.XPATH, '//a[contains(@href, "allergy")]')

#This webpage is old and ugly, so we have to scrape it using fuzzy matching
#Get variations for synonym target phrase
target_variations = [
    "Other names you may see this chemical listed as:",
    "Other names you may see this product listed as:",
    "Other names for this chemical include:",
    "Alternate names for this product:"
]

#Create an empty dataframe to store allergens and synonyms
df = pd.DataFrame(columns=["Name", "Synonyms"])

#Loop through each allergen link
for i in range(len(allergen_links)):

    #Re-fetch the links since the page reloads after navigating
    allergen_links = driver.find_elements(By.XPATH, '//a[contains(@href, "allergy")]')

    #Click on the current link
    allergen_name = allergen_links[i].text
    print(f"Processing allergen: {allergen_name}")

    allergen_links[i].click()
    time.sleep(3)

    #Parse the new page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    #Get all visible text on page and find the best match
    all_texts = [text for text in soup.stripped_strings]
    print(all_texts)
    best_match, score = process.extractOne("Other names", all_texts)

    if score > 80:  #We'll set this as the threshold for matching
        print(f"Found target phrase: {best_match} (Score: {score})")

        #Find the position of the best match in the text
        start_index = all_texts.index(best_match) + 1

        #Extract synonyms appearing after the heading
        synonyms = []
        for text in all_texts[start_index:]:
            #Telling it where to stop parsing
            if text == "" or "Where is it found?" in text or "Contact Us" in text or "Possible Occupational Exposures" in text:
                break
            synonyms.append(text)

        #Store synonyms as a list
        synonyms_str = ", ".join(synonyms)

        #Append the dataframe
        df.loc[len(df)] = [allergen_name, synonyms_str]

        #Print results
        print("Synonyms found:")
        for synonym in synonyms:
            print(synonym)
    else:
        print("Target phrase not found on this page.")

    #Go back to the main allergen list
    driver.back()
    time.sleep(2)  # Wait for the page to reload

#Save the dataframe
df.to_csv("allergen_synonyms.csv", index=False)

#Close the driver
driver.quit()
