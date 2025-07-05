from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = Options()
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


driver = webdriver.Chrome(options=options)

driver.get("https://www.glassdoor.com/Job/texas-data-science-jobs-SRCH_IL.0,5_IS1347_KO6,18.htm")
number = 1

WebDriverWait(driver, 15).until(
EC.presence_of_element_located((By.CLASS_NAME, "JobCard_jobCardContainer__arQlW"))
)

cards = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardContainer__arQlW")
for card in cards:
    html = card.get_attribute("outerHTML")
    with open(f"data/file{number}.html", "w") as f:
        f.write(html)
        number = number + 1

    




driver.close()
