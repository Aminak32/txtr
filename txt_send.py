#!/usr/bin/python

import sys
import json
from grind_txts.util import Texter, ingest_grind_csv
from grind_txts.constants import EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR

def get_grind_members():
    members = []
    with open('grind_members.json') as f:
        members = json.load(f)
    return members


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'ingest':
            print ingest_grind_csv(sys.argv[2]) # sys.argv[2] is the filepath of the grind csv

        else:
            m = sys.argv[1]
            texter = Texter(EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR)
            grind_members = get_grind_members()
            for g in grind_members:
                to_addr = Texter.get_to_addr(g['number'], g['carrier'])
                texter.SMS_send(to_addr, m)
    else:
        pass
