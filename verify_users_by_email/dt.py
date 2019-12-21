from datetime import timedelta, datetime as dt, date
from db import list_users, query_user_last_seen
import time

def main():
    username = get_mail(attempts = 3, pause = 10)
    check_user_is_active(username, list_users, query_user_last_seen)

#ask e-mail, with limited attempts
def get_mail(attempts, pause):
    mail = input("Provide your e-mail: ")
    i = 1
    while (mail.find("@") == -1):
        print("Wrong e-mail, try again")
        i += 1
        mail = input("Attempt " + str(i) + "Provide your e-mail: ")
        if i % attempts == 0:
            print("Too much attempts. Wait for " + str(pause) + " second")
            time.sleep(pause)
    username = mail.split("@")[0].lower()
    return username

def check_user_is_active(username, list_users, query_user_last_seen):
    known_users = list_users()
    for i in known_users:
        if username == i[0]:
            last_seen = query_user_last_seen(username)
            if dt.now() - last_seen <= timedelta(days = 180):
                print("Your account is confimed. Your account is valid till " + str(date.today() + timedelta(days = 180)))
            elif dt.now() - last_seen >= timedelta(days = 180):
                print("You need to confirm your login")
        elif (not i in known_users):
            print("Hi, new user")


if __name__ == "__main__":
    main()