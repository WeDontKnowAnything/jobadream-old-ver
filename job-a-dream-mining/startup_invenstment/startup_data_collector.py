from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from .constants import STARTUP_COLUMNS, STARTUP_URL, DATA_DIR
import csv
import re
import os


##### 수정필요
class StartupCollector:
    def __init__(self, last_page: int) -> None:
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.options)
        self.last_page = last_page
        self.url = STARTUP_URL + str(self.last_page)

    def init_driver(self) -> None:
        # Set browser zoom level to 50%
        self.driver.get("chrome://settings/")
        self.driver.execute_script("chrome.settingsPrivate.setDefaultZoom(0.5);")
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def str2int(self, string: str) -> int:
        # Regular expression to find numbers and '만' unit
        match = re.match(r"(\d+(\.\d+)?)(만|천)?", string)
        if match:
            integer = float(match.group(1))  # Extract the numeric part
            unit = match.group(3)  # Extract the unit part ('만' or '천')

            if unit == "만":
                return int(integer * 10000)
            elif unit == "천":
                return int(integer * 1000)
            else:
                return int(integer)

    def collect_startup_data(self) -> list[dict]:
        corporations_details = []
        parserd_items = self.driver.find_elements(By.CLASS_NAME, "css-0")
        for idx, parserd_item in enumerate(parserd_items[2:]):
            # Collect corporation & product
            corp_prod = parserd_item.find_element(By.CLASS_NAME, "css-14o0uv")
            corporation = corp_prod.find_element(By.CLASS_NAME, "corp")
            product = corp_prod.find_element(By.CLASS_NAME, "prod")
            # Collect the rest of the data
            description = parserd_item.find_element(By.CLASS_NAME, "css-e0dnmk")
            investment_round = parserd_item.find_element(
                By.XPATH,
                f'//*[@id="__next"]/main/div/div[2]/div/article[2]/table/tbody/tr[{idx+1}]/td[3]',
            )
            revenue_employee = parserd_item.find_elements(By.CLASS_NAME, "css-1ytuqjc")
            parserd_keywords = parserd_item.find_elements(By.CLASS_NAME, "css-1u4hpl4")
            keywords = [parserd_keyword.text for parserd_keyword in parserd_keywords]

            COLUMNS = STARTUP_COLUMNS
            corporations_details.append(
                {
                    COLUMNS.CORPORATION.value[1]: corporation.text.split("\n")[0],
                    COLUMNS.PRODUCT.value[1]: product.text,
                    COLUMNS.DESCRIPTION.value[1]: description.text,
                    COLUMNS.INVESTMENT_ROUND.value[1]: investment_round.text,
                    COLUMNS.TOTAL_INVESTMENT.value[1]: revenue_employee[0].text,
                    COLUMNS.REVENUE.value[1]: revenue_employee[1].text,
                    COLUMNS.EMPLOYEE_NUM.value[1]: self.str2int(
                        revenue_employee[2].text
                    ),
                    COLUMNS.KEYWORD.value[1]: "".join(keywords),
                }
            )
        self.driver.quit()
        return corporations_details

    def save_csv(self, corporations_details: list[dict]) -> None:
        # Set the current version to 'Date'
        version = datetime.today().strftime("%Y%m%d")
        # Change current directory to 'job-a-dream-mining/data'
        os.chdir(DATA_DIR)
        data_directory = os.getcwd()
        csv_file = os.path.join(data_directory, f"test_Startup_Data_{version}.csv")

        # Check if the CSV file exists in the drectory
        is_file = os.path.isfile(csv_file)
        csv_columns = [column.value[1] for column in STARTUP_COLUMNS]
        try:
            with open(csv_file, "a", newline="", encoding="utf-8-sig") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                # Create a CSV file if the CSV file doesn't exist
                if not is_file:
                    writer.writeheader()
                for corporation_detail in corporations_details:
                    writer.writerow(corporation_detail)
            print(f"{self.last_page} page: Data successfully saved to {csv_file}")
        except IOError as e:  # Path Error, when save the CSV file
            print(
                f"Error saving to file: {e}. Please check the 'job-a-dream-mining/data' directory."
            )

    def start_collecter(self) -> None:
        for self.last_page in range(1, self.last_page + 1):
            self.init_driver()
            corporations_details = self.collect_startup_data()
            self.save_csv(corporations_details)
