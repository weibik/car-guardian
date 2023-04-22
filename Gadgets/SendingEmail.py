import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

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


def send_email_with_file():
    # Tworzenie treści wiadomości
    message = MIMEMultipart()
    message['Subject'] = 'Raport SafetyCar 04/05.2023'
    message['From'] = 'hachatonagh123@gmail.com'
    message['To'] = 'wojtek.pasiu@gmail.com'
    text = MIMEText('Wiadomość wygenerowana automatycznie.')
    message.attach(text)

    # Dodawanie załącznika
    filename = "C:/Users/Dell/Desktop/hackaton/car-guardian/Gadgets/CarSafety raport.pdf"
    with open(filename, 'rb') as file:
        attach = MIMEApplication(file.read(), _subtype='pdf')
        attach.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(attach)

    # Wysyłanie wiadomości e-mail
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('hachatonagh123@gmail.com', 'vlmpfaflxnvuudfp')
        smtp.send_message(message)
