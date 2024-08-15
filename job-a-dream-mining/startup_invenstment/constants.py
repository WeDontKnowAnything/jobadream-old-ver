import enum

# 'data' folder directory
DATA_PATH = './job-a-dream-mining/data'

# stratup investment information '혁신의 숲' url
STARTUP_URL = "https://www.innoforest.co.kr/dataroom?page="

# csv columns
class STARTUP_COLUMNS(enum.Enum):
    CORPORATION = (enum.auto(), 'corporation')
    PRODUCT = (enum.auto(), 'product')
    DESCRIPTION = (enum.auto(), 'description')
    INVESTMENT_ROUND = (enum.auto(), 'investment_round')
    TOTAL_INVESTMENT = (enum.auto(), 'total_investment')
    REVENUE = (enum.auto(), 'revenue')
    EMPLOYEE_NUM = (enum.auto(),'employee_num')
    KEYWORD = (enum.auto(), 'keyword')
