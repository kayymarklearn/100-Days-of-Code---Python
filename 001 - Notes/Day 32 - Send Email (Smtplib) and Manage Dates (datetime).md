2026-01-24 21:59

Status:

Tags: [[Day 32 - Send email (smtplib) and Manage Dates (datetime) (code)]]


# **Day 32 - Send Email (Smtplib) and Manage Dates (datetime)**
## How Exactly does Email work?
> A mail server will receive the message from sender and another mail server which stores the sent mail till the receiver logs in and views it. The protocol that allows all this is called SMTP (Simple Mail Transfer Protocol). In python the module 'smtplib' which allows us to use this protocol to send and receive email.

#### Usage of smtplib
```
import smtplib

  

my_email = "random_mail@gmail.com"

password="abcd1234()" # Generated in email account settings

with smtplib.SMTP("smtp.gmail.com") as connection: # .SMTP is different for all mail services

connection.starttls()

connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email,

to_addrs="another_random_mail@gmail.com",

msg="Subject: Hello\n\nThis is the body of the email."

)

# connection.close()
```

#### Usage of datetime 
```
import datetime as dt

now = dt.datetime.now() # Get current date and time

year = now.year # Get the current year

month = now.month

weekday = now.weekday() # Returns the current day of week 1 = monday, 5 = friday

date_of_birth = dt.datetime(year=2001, month=12, day=21)

print(date_of_birth)
```
## References
