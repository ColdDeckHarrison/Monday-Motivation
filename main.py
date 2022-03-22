import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quote.txt", "r") as quotes_file:
        file = quotes_file.readlines()
        quote_of_the_day = random.choice(file)
    my_email = "pythonautomail87@gmail.com"
    my_password = "Password"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email",
                            msg=f"subject:Inspirational Monday\n\n {quote_of_the_day}"
        )

