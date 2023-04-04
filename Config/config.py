import datetime
x = datetime.datetime.today().strftime("%m%d%Y%H%M%S%I")
class TestData:
    DRIVER_PATH = r'D:\ref\templates\Python Codes\VODEX\driver\chromedriver_win32\chromedriver.exe'
    EDGE_PATH = r'D:\ref\templates\Python Codes\VODEX\driver\edge_driver\msedgedriver.exe'
    BASE_URL = "https://preprod.vodex.ai/"
    # BASE_URL = "https://preprod.vodex.ai/"
    USER_NAME = "proxy@3003.io"
    PASSWORD = "123456"
    AUDIENCE_NAME = "Daddy"+x[-6:]
    FIRST_NAME = "Daddy"
    LAST_NAME = "Allu"
    PHONE_NUM = "1234567890"
    PHONE_NUM_DROPDOWN = "Manually add Numbers"
    CAMPAIGN_NAME = "Campaign"+x
    GREET_TAG_NAME = "greeting"
