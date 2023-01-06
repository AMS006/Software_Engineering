from http import server
import smtplib;
import random;

server = smtplib.SMTP('smtp.gmail.com', 587);
server.starttls()
myemail = 'anassain2002@gmail.com'
password = 'tyfqxwmnvxlakudg'
server.login('anassain2002@gmail.com',"tyfqxwmnvxlakudg");
otp = random.randrange(100000,1000000);
message = "Otp to login to your account is " + str(otp);
tosend = input("Enter your email id : ")
server.sendmail("anassain2002@gmail.com",tosend, message );
server.quit();

isCorrectOtp = int(input(("Enter your Otp : ")));
if(isCorrectOtp == otp):
   print("Loged in Successfully");
else:
   print("Invalid Otp")