import csv
import json
import smtplib
from grind_txts.constants import CARRIER_MAP

def ingest_grind_csv(csv_name):
    grind_list = list()
    with open(csv_name) as f:
        reader = csv.DictReader(f, fieldnames=['timestamp', 'name', 'number', 'carrier'])
        header = reader.next()
        for row in reader:
            del row['timestamp']
            row['carrier'] = row['carrier'].lower().strip()

            # some quick naming adjustmenst for carriers to map well
            if row['carrier'] == 'at&t':
                row['carrier'] = 'att'
            if row['carrier'] == 'virgin mobile':
                row['carrier'] = 'virgin'
            if row['carrier'] == 'boost mobile':
                row['carrier'] = 'boost'

            grind_list.append(row)

    with open('grind_members.json', 'w') as f:
        json.dump(grind_list, f)

    return grind_list


class Texter(object):

    def __init__(self, username, passwd, email_addr):
        self.user = username
        self.passwd = passwd
        self.addr = email_addr

    def SMS_send(self, to_addr, message):
        '''
        function takes a to_address and the message to send
        use the get_to_addr() function below to get the to_address
        '''

        # The actual mail send
        mail_server = smtplib.SMTP('smtp.gmail.com:587')
        mail_server.starttls()
        mail_server.login(self.user, self.passwd)
        mail_server.sendmail(self.addr, to_addr, message)
        mail_server.quit()

    @classmethod
    def get_to_addr(cls, number, carrier):
        '''
        function takes two strings, the 10-digit phone number and the cell carrier
        if you need to see how to format the carrier name, check CARRIER_MAP in grind_txts/constants.py
        '''
        return "%s@%s" % (str(number), CARRIER_MAP[carrier])
