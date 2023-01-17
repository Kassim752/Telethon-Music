import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5864142861:AAHRGgDQnqDoWaHhP0k_ginuFMpeuDBmrPk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBu2K5Yr_rcSD78_vI3dcihE7sQY-klz0M7R_N0BgMx7a5MW4HlMkh0Ja1qzz5vma8MIR16fSBQosnW3T_6z7-xdVLUGFfGdhl1p4bQFoHkwmx0ilpCstnhhxM53j_CqPe-1TtYsqlMwCSU_gAr2tcHNmqz39EHQ2QSpvvLOg8U1bZzQMNn5X8FBGRblUq5umvTqRhRynbfgfcAQEc-6pa7MbKxNij2SxXSLmUX-3N6uW7LsJF3at6czfnHq8w8-6fmECZdry3_0tzU1gXMdf0paGrEmxQDQKEuXg4vnMAG-If-gaje8xO9b4WROckM-DIfOABZSPp4vQflQJaNuzB5i8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("WizkhalifaBot")
    SUPPORT = os.environ.get("SUPPORT", "l_Cuddle_Buddy_l") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Wizkhalifa_channel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("5809469335")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
