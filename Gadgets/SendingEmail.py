import smtplib

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'hachatonagh123@gmail.com'
password = 'vlmpfaflxnvuudfp'
receiver_email = 'jan.krol.legowski@gmail.com'

# Create the message
message = """\
Subject: Car Alert

This message is send automatically to inform you that your car is drived by , which increase the risk of stluczka and rozjebane sprzeglo.
"""

# Log in to the SMTP server
server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, password)

# Send the email
server.sendmail(sender_email, receiver_email, message)

# Log out of the SMTP server
server.quit()