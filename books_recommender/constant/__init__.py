import os

# ek question yeh arise hota hai ki yeh sab kyu kar rhe hai


ROOT_DIR = os.getcwd() # iska matlab

# main config file path
CONFIG_FOLDER_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FOLDER_NAME, CONFIG_FILE_NAME)