
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, comment_text,post_link):
    # Email content
    subject = "Negative Comment Notification"
    body = f"Hello,\n\nYou have received a negative comment on your Instagram post:\n\n{comment_text}\n\n{post_link}\n\nBest regards,\nYour Social Media Team"

    # Setup the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach body to the email
    message.attach(MIMEText(body, "plain"))

    # Establish a secure session with the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print('Mail sent')
    # Close the server connection
    server.quit()



