# =============================
# 📁 LOGGING CONFIGURATION FILE
# =============================
# This script sets up logging for your Python project.
# It creates a timestamped `.log` file inside a 'logs' folder,
# so every time your project runs, logs are saved in a clean,
# organized, and trackable way. Useful for debugging and monitoring.
# =============================

import logging
import os
from datetime import datetime

# 🔹 Create a log filename using current timestamp (e.g., 05_23_2025_18_30_45.log)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 🔹 Define the 'logs/' folder path inside your current working directory
logs_path = os.path.join(os.getcwd(), "logs")

# 🔹 Create the 'logs/' folder if it doesn't exist already
os.makedirs(logs_path, exist_ok=True)

# 🔹 Full path where the log file will be saved
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 🔹 Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# # 🔹 Testing the logger
# if __name__ == "__main__":
#     logging.info("✅ Logging has started successfully!")
#     logging.warning("⚠️ This is a warning log.")
#     logging.error("❌ This is an error log.")
#     print(f"Log file created at: {LOG_FILE_PATH}")
