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
    parser.add_argument('-i', '--ingest', action="store_true", default="False",
                        help='csv file for ingestion')
    parser.add_argument('-m' '--message', help='the message you wish to send')
    args = parser.parse_args()


    if args.ingest:
        # sys.argv[2] is the filepath of the member csv
        print ingest_user_csv(sys.argv[2])

    else:
        msg = sys.argv[1]
        texter = Texter(EMAIL_USERNAME, EMAIL_PASSWD, EMAIL_ADDR)
        members = load_members()
        for m in members:
            to_addr = Texter.get_to_addr(m['number'], m['carrier'])
            texter.SMS_send(to_addr, msg)
