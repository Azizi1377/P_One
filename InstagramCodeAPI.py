from fastapi import FastAPI, Query
from curses.ascii import isdigit
import imaplib
import email


app = FastAPI()


@app.get("/InsCode")
def FetchInstagramCode(
    user: str = Query(default=..., description="Enterr your email!"),
    password: str = Query(default=..., description="Enterr Your Password Devais!"), 
    key: str = Query(default=..., description="Enterr your email Key!"), 
    value: str = Query(default=..., description="Enterr Adress email destination!")
    ):
 

    # key = 'FROM'  
    # value = 'no-reply@mail.instagram.com'
    # user = "2m.2a.1221@gmail.com"
    # password = "edhkygoygfpncxtu"

    my_mail = imaplib.IMAP4_SSL('imap.gmail.com')
    my_mail.login(user,password)
    my_mail.select('Inbox')

    
    _, data = my_mail.search(None, key, value)  #Search for emails with specific key and value
    mail_id_list = data[0].split()  #IDs of all emails that we want to fetch 
    msgs = [] # empty list to capture all messages

    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)') #RFC822 returns whole message (BODY fetches just body)
        msgs.append(data)
        

    num0=1;
    AllSubjects=[];
    for msg in msgs[::-1]:
        for response_part in msg:
            if type(response_part) is tuple:
                my_msg=email.message_from_bytes((response_part[1]))
                AllSubjects=my_msg['subject']
                AllSubjects=str(AllSubjects)
                InsNum=AllSubjects[0:6];
                if isdigit(InsNum[1]):
                    print(InsNum)
                    FetchedCode=InsNum
            break
        break
        
    return {FetchedCode}