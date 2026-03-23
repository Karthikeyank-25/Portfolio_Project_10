# IMPORTING PACKAGES :
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# KEEPING CHROME PAGE OPEN :
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# AUTOMATING PROCESS :
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.nba.com/")

# PROCESS SETTING :
wait = WebDriverWait(driver, 15)
# GETTING INTO STATS :
stats = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Stats']]")))
stats.click()
# CLOSING POPUP BOX :
pop_up = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
pop_up.click()
# CHOOSING PLAYERS DETAILS :
player = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Players']]")))
player.click()
# GETTING INTO PLAYER'S TRADITIONAL STATS :
traditional_data = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Traditional Stats')]")))
traditional_data.click()
time.sleep(10)
# FINDING TABLE :
rows = driver.find_elements(By.XPATH, "//table//tbody/tr")
time.sleep(10)
all_data = []
time.sleep(10)
# EXTRACTING EACH ROWS DATA :
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    if len(row_data) > 1 and row_data[1] != "":
        print(row_data)
        all_data.append(row_data)
    else:
        print("No data found")
headers = ['Rank', 'Player', 'Team', 'Age', 'GP', 'W', 'L', 'Min', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'PF', 'FP', 'DD2', 'TD3', '+/-']
# CREATING CSV FILE :
with open('nba_stats.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # SETTING HEADERS TO CSV FILE :
    writer.writerow(headers)
    for row in all_data:
        if row and row[0] != '':
            # INCLUDING DATA TO CSV FILE :
            writer.writerow(row)
        else:
            print("No data found")
# COMPLETION OF THE PROJECT :
print("Project Complete! Your CSV is ready.")