#!/usr/bin/python

import sys
import json
from txtr.util import Texter, ingest_user_csv
from txtr.constants import EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR

def get_members():
    members = []
    with open('members.json') as f:
        members = json.load(f)
    return members


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'ingest':
            # sys.argv[2] is the filepath of the member csv
            print ingest_user_csv(sys.argv[2])

        else:
            msg = sys.argv[1]
            texter = Texter(EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR)
            members = get_members()
            for m in members:
                to_addr = Texter.get_to_addr(m['number'], m['carrier'])
                texter.SMS_send(to_addr, msg)
    else:
        pass
