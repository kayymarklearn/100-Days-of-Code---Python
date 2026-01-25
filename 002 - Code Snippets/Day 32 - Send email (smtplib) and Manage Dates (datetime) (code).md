2026-01-24 21:59

Status: Incomplete

Tags: [[Day 32 - Send Email (Smtplib) and Manage Dates (datetime)]]

## Sending motivational quotes every monday using smtplib and datetime
```
import smtplib

import datetime as dt

from random import choice


MY_EMAIL = "random_mail@gmail.com"

MY_PASSWORD="abcd1234()"

now = dt.datetime.now()

current_day_of_week = now.weekday()
  

if current_day_of_week == 1:

with open("quotes.txt", 'r') as file:

content = file.readlines()


message = choice(content).split("-")

subject = message[1].strip()

quote = message[0]

with smtplib.SMTP("smtp.gmail.com") as connection:

connection.starttls()

connection.login(user=MY_EMAIL, password=MY_PASSWORD)

connection.sendmail(from_addr=MY_EMAIL,

to_addrs=MY_EMAIL,

msg=f"Subject: Monday Motivation by {subject}\n\n{quote}"

)
```

