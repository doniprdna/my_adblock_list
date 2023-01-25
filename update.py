import os
import schedule
import time

def update_adblock_list():
    os.system("python /path/to/adblock_update.py")

schedule.every().day.at("00:00").do(update_adblock_list)

while True:
    schedule.run_pending()
    time.sleep(1)
