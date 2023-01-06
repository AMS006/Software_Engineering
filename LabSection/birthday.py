import datetime
import pandas as pd
import smtplib
import os
os.chdir(r"C:\SE-Practical-Exam")

def sendEmail(to,sub,msg):
    server = smtplib.SMTP('smtp.gmail.com', 587);
    server.starttls()
    server.login('anassain2002@gmail.com',"tyfqxwmnvxlakudg");
    server.sendmail("anassain2002@gmail.com",to,f"Subject: {sub}\n\n{msg}");
    server.quit();

if __name__ == "__main__":

    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    year = datetime.datetime.now().strftime("%Y")
    # Excel Data
    print(df)
    for index,item in df.iterrows():
        birthday = item['Birthday'].strftime("%d-%m")
        if today == birthday:
            print(item['Email'])
            sendEmail(item['Email'],"Happy Birthday",item['Dialogue'])
            

