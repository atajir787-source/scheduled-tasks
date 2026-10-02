import os
import smtplib
import random
from datetime import datetime

my_mail = os.environ.get("MY_MAIL")
my_password = os.environ.get("MY_PASSWORD")

now = datetime.now()

today = (now.month, now.day)
import pandas
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)
for today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        replaced_matter =content.replace("[NAME]", birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{replaced_matter}")











