#!/usr/bin/python3.6
from slackclient import SlackClient
import os
import argparse

def createUserSlack(email, firstname, secondname):
    with open(os.path.expanduser(os.environ['SLACK_BOT_TOKEN'])) as file:
        SLACK_BOT_TOKEN = file.readline().split()[0]
    if (SLACK_BOT_TOKEN == "" or SLACK_BOT_TOKEN == None): return {"ok": False, "error": "Error read token for slack"}
    sc = SlackClient(SLACK_BOT_TOKEN)
    responce = sc.api_call(
        "users.admin.invite",
        email=email,
        first_name=firstname,
        last_name=secondname
    )
    return responce
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', action='store', type=str, default='')
    parser.add_argument('--firstname', action='store', type=str, default='')
    parser.add_argument('--secondname', action='store', type=str, default='')
    parameters = parser.parse_args()

    responce = createUserSlack(email=parameters.email, firstname=parameters.firstname, secondname=parameters.secondname)
    if (not responce['ok']):
        print(responce['error'])
    else:
        print(responce['ok'])
if __name__ == '__main__':
    main()