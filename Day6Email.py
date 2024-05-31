# cutq xwja uuoz jrwv
import smtplib
try:
    server=smtplib.SMTP(host='SMTP.gmail.com',port=587)
    server.starttls()
    receiver_email=input("enter email of the receiver")
    sender_email="kumarsainiaashish2003@gmail.com"
    passwd ="cutq xwja uuoz jrwv"
    server.login(sender_email,password=passwd)
    subject=input("What is your problem ?")
    body=input("Explain in detail")
    message=f"subject: {subject}\n\n{body}"
    server.sendmail(sender_email,receiver_email,message)
    print("Successfully sended the mail")
    server.quit()
except Exception as e:
    print("mail is not sended ",e) 

    