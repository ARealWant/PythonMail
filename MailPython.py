# Before you start, read the README (https://github.com/ARealWant/PythonMail)
# Developed by https://github.com/ARealWant/

    port = 465  # For starttls
    smtp_server = "MAIL-SERVER"
    sender_email = "MAILER"
    receiver_email = "REVEICER"
    password = input("Type your password and press enter:")
    message = "MESSAGE"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
