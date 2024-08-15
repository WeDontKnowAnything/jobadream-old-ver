from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import constants
import csv
import re
import os

def init_driver() -> webdriver.Chrome:
    driver = webdriver.Chrome()
    # Set browser zoom level to 50%
    driver.get("chrome://settings/")
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.5);')
    return driver

def str2int(string: str) -> int:
    # Regular expression to find numbers and '만' unit
    match = re.match(r'(\d+(\.\d+)?)(만|천)?', string)
    if match:
        integer = float(match.group(1))  # Extract the numeric part
        unit = match.group(3)  # Extract the unit part ('만' or '천')
        
        if unit == '만':
            return int(integer * 10000)
        elif unit == '천':
            return int(integer * 1000)
        else:
            return int(integer)

def collect_startup_data(driver: webdriver.Chrome, page: int) -> list[dict]:
    url = constants.STARTUP_URL + str(page)
    driver.get(url)
    driver.implicitly_wait(3)
    
    corporations_details = []
    parserd_items = driver.find_elements(By.CLASS_NAME, "css-0")
    for idx, parserd_item in enumerate(parserd_items[2:]):
        # Collect corporation & product
        corp_prod = parserd_item.find_element(By.CLASS_NAME, "css-14o0uv")
        corporation = corp_prod.find_element(By.CLASS_NAME, "corp")
        product = corp_prod.find_element(By.CLASS_NAME, "prod")
        # Collect the rest of the data
        description = parserd_item.find_element(By.CLASS_NAME, "css-e0dnmk")
        investment_round = parserd_item.find_element(By.XPATH, f'//*[@id="__next"]/main/div/div[2]/div/article[2]/table/tbody/tr[{idx+1}]/td[3]')
        revenue_employee = parserd_item.find_elements(By.CLASS_NAME, "css-1ytuqjc")
        parserd_keywords = parserd_item.find_elements(By.CLASS_NAME, "css-1u4hpl4")
        keywords = [parserd_keyword.text for parserd_keyword in parserd_keywords]
        
        COLUMNS = constants.STARTUP_COLUMNS
        corporations_details.append({
            COLUMNS.CORPORATION.value[1]: corporation.text.split('\n')[0],
            COLUMNS.PRODUCT.value[1]: product.text,
            COLUMNS.DESCRIPTION.value[1]: description.text,
            COLUMNS.INVESTMENT_ROUND.value[1]: investment_round.text,
            COLUMNS.TOTAL_INVESTMENT.value[1]: revenue_employee[0].text,
            COLUMNS.REVENUE.value[1]: revenue_employee[1].text,
            COLUMNS.EMPLOYEE_NUM.value[1]: str2int(revenue_employee[2].text),
            COLUMNS.KEYWORD.value[1]: ''.join(keywords),
        })
    driver.quit()
    return corporations_details

def save_csv(corporations_details: list[dict], page: int) -> None:
    # Set the current version to 'Date-Time'
    version = datetime.today().strftime("%Y%m%d_%Hh%Mm")
    # Change current directory to 'job-a-dream-mining/data'
    os.chdir(constants.DATA_PATH)
    data_directory = os.getcwd()
    csv_file = os.path.join(data_directory, f"Startup_Data_{version}.csv")

    # Check if the CSV file exists in the drectory
    is_file = os.path.isfile(csv_file)
    csv_columns = [column.value[1] for column in constants.STARTUP_COLUMNS]
    try:
        with open(csv_file, 'a', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            # Create a CSV file if the CSV file doesn't exist
            if not is_file:
                writer.writeheader()
            for corporation_detail in corporations_details:
                writer.writerow(corporation_detail)
        print(f"{page} page: Data successfully saved to {csv_file}")
    except IOError as e: # Path Error, when save the CSV file
        print(f"Error saving to file: {e}. Please check the 'job-a-dream-mining/data' directory.")

def main() -> None:
    last_page = 508 # 추후 CLI 입력으로 바꿀 것
    for page in range(1, last_page+1):
        driver = init_driver()
        corporations_details = collect_startup_data(driver, page)
        save_csv(corporations_details, page)

if __name__ == "__main__":
    main()