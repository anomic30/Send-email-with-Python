#####################################################################################
##              Simple program to send email to anyone using Python                ##
##              Author: Anom Chakravorty | Github: anomic30                        ##
#####################################################################################
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

email = input("Enter your Gmail: ")
password = input('Enter your app password!')
server.login(email, password)

from_address = email
to_address = input("Enter receiver's email address: ")
subject = input("Enter the subject: ")
message = input("Enter the message: ")
msg = "Subject: " + subject + '\n' + message

server.sendmail(from_address, to_address, msg)
print("Mail sent successfully")

server.quit()