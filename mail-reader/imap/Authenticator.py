'''
# Using secure IMAP to connect to mail Server and fetch the Mails
'''

import imaplib as im
from email.parser import HeaderParser
import csv
from imap.Credentails import credentials

folders = ['Inbox', '"[Gmail]/Spam"']

def authenticate(mail_server="imap.gmail.com"):
    with open('mail.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for t in credentials:
            print('Logging into mailId : '+t[0])
            M = im.IMAP4_SSL(mail_server, im.IMAP4_SSL_PORT)
            result,auth = M.login(t[0],t[1])
            if result == 'NO':
                print("Login Failed!!!")
                continue
            parser = HeaderParser()
            for folder in folders:
                rs,num = M.select(folder,True)
                print("Result : "+rs+", Num: "+str(num[0]))
                if rs == 'NO':
                    print("Unable to Access Folder : " + folder)
                    continue
                totalMails = int(num[0])
                success, data = M.uid('search', 'SUBJECT', 'Undeliverable:')
                #success, data = M.uid('search', 'SUBJECT', '(HEADER Subject "Undeliverable:")')
                if success == 'NO':
                    print("Search result was un-successful")
                    continue
                idList = data[0].split()
                print("Id List : "+str(idList)+", Lenght: " + str(len(idList)))
                for uid in idList:
                    rst, data = msgDetails = M.uid('fetch', uid, '(FLAGS BODY[HEADER.FIELDS (DATE FROM SUBJECT Delivered-To X-Failed-Recipients TO)])')
                    #data = M.fetch(i,'(BODY[HEADER])')
                    header_data = data[0][1]
                    #header_data = data[1][0][1]
                    headerMap = parser.parsestr(header_data.decode("utf-8"))
                    print(headerMap.keys())
                    x_failed_recipients = headerMap.get('X-Failed-Recipients')
                    print(x_failed_recipients)
                    list = []
                    if x_failed_recipients is not None:
                        list.append(x_failed_recipients)
                    wr.writerow(list)
                #M.logout()

if __name__ == '__main__':
    authenticate()
