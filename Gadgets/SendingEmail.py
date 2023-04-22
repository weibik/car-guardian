import smtplib

from CarInfo.CarInfo import set_location


def send_email():
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'hachatonagh123@gmail.com'
    password = 'vlmpfaflxnvuudfp'
    receiver_email = 'wojtek.pasiu@gmail.com'

    location = set_location()

    polish_chars = "ąćęłńóśźż"
    english_chars = "acelnoszz"
    translation_table = str.maketrans(polish_chars, english_chars)

    translated_location = location.translate(translation_table)

    message = f"""\
    Temat: Car Alert

    Your car is active.
        Current location: 
        {translated_location}

        This message is send automatically.
                    Safety Car
    """


    # Log in to the SMTP server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message)

    # Log out of the SMTP server
    server.quit()