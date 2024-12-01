import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# from email.mime import text, multipart, base # another method

from email.header import Header
from email import encoders

sender = "hanke.tseng@gmail.com"
receiver = "hanke_tseng@hotmail.com"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = Header("你好! This is Python mail sending test", "utf-8").encode()

content = MIMEText("這是內容測試")
msg.attach(content)

""" starting point of Attachement processing"""
# with open("test.txt",'rb') as f:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(f.read())
#     encoders.encode_base64(part) # 檔案加密
#     part.add_header("Content-Disposition",'attachment; filename="test.txt"')
# msg.attach(part)

# with open("Python send email.pdf",'rb') as f:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(f.read())
#     encoders.encode_base64(part) # 檔案加密
#     part.add_header("Content-Disposition",'attachment; filename="Python send email.pdf"')
# msg.attach(part)

# 假如有中文的檔名的處理方式
with open("test.txt",'rb') as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
    encoders.encode_base64(part) # 檔案加密
    header = Header("中文.txt","utf-8").encode() # 假如有中文的檔名的處理方式
    part.add_header("Content-Disposition",'attachment; filename="' + header + '"') # ' ' 括住"字串
msg.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender,"dieoqpzdvkryohtu")
    server.sendmail(sender, receiver, msg.as_string())
print("Mail sent successfully!!!")

