import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # SMTP server configuration (example using Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Email content setup
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # Login authentication
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        
        print("Email sent successfully.")
    
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
    
    finally:
        # Close the SMTP connection
        server.quit()

# User input for email details
sender_email = input("Sender's email address: ")
sender_password = input("Sender's email password: ")
receiver_email = input("Receiver's email address: ")
subject = input("Email subject: ")
message = input("Email content: ")

# Call the send_email function to send the email
send_email(sender_email, sender_password, receiver_email, subject, message)
