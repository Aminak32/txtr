#!/usr/bin/python

import sys
import json
import argparse
from txtr.util import Texter, ingest_user_csv
from txtr.constants import EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR

def load_members():
    members = []
    with open('members.json') as f:
        members = json.load(f)
    return members


if __name__ == '__main__':

    # define command line args
    parser = argparse.ArgumentParser(description="mass texting module")
    parser.add_argument('-i', '--ingest',
                        help='csv file for ingestion of users numbers and carriers')
    parser.add_argument('-m', '--message',
                        help='the message you wish to send')
    args = parser.parse_args()


    if args.ingest:
        print ingest_user_csv(args.ingest)

    elif args.message:
        msg = args.message
        texter = Texter(EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR)
        members = load_members()
        for m in members:
            to_addr = Texter.get_to_addr(m['number'], m['carrier'])
            texter.SMS_send(to_addr, msg)

    else:
        print "sorry, you must either provide a csv file to ingest or provide a message to send"
