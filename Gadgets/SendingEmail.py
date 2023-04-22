import smtplib
#nie dziala przez gmaila xDD
# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'hachatonagh123@gmail.com'
password = 'Qwerty123chuj'
receiver_email = 'szkolka00@gmail.com'

# Create the message
message = """\
Subject: Car Alert

This message is send automatically to inform you that your car is drived by BABA, which increase the risk of stluczka and rozjebane sprzeglo.
"""

# Log in to the SMTP server
server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, password)

# Send the email
server.sendmail(sender_email, receiver_email, message)

# Log out of the SMTP server
server.quit()