#!/usr/bin/python

import sys
import json
import argparse
from txtr.util import Texter, ingest_user_csv
from txtr.constants import EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR

def load_members(filename):
    members = []
    with open(filename) as f:
        members = json.load(f)
    return members

def send_txt(message, filename):
    texter = Texter(EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR)
    members = load_members(filename)
    for m in members:
        to_addr = Texter.get_to_addr(m['number'], m['carrier'])
        texter.SMS_send(to_addr, msg)


if __name__ == '__main__':

    # define command line args
    parser = argparse.ArgumentParser(description="mass texting module")
    parser.add_argument('-i', '--ingest', action="store_true", default=False,
                        help='ingestion of users numbers and carriers')
    parser.add_argument('-m', '--message',
                        help='the message you wish to send')
    parser.add_argument('-f', '--filename', required=True
                        help='the name of the json file containing recipients or the csv file to ingest')
    args = parser.parse_args()


    if args.ingest:
        print ingest_user_csv(args.filename)
    elif args.message:
        send_txt(args.message, args.filename)

    else:
        print "sorry, you must either provide a csv file to ingest or provide a message to send"
