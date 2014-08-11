#!/usr/bin/env python
# encoding: utf-8


# description
# TODO: documentation


# imports
import sys
import socket
import string
import time
import json
import random

from commands import rejoin, uptime, gif


# settings
s = socket.socket()
channels = ['#weezky', '#jhgrng']
modes = ['PRIVMSG', 'KICK']
time_at_start = time.time()


# quotes
quotes_file = open('quotes.json').read()
quotes = json.loads(quotes_file)


# functions
def setup():
    # TODO: documentation
    '''

    '''


    host = "irc.quakenet.net"
    port = 6667
    nick = "weezky"

    s.connect(('irc.quakenet.org', 6667))
    s.send("NICK %s\r\n" % nick)
    s.send("USER %s %s bla :%s\r\n" % (nick, nick, nick))


def display_hello_message():
    # TODO: documentation
    '''
    '''


    print("\nHello!\n\n\n")


def parse_sender_info(sender):
    # TODO: documentation
    '''
    '''


    for i, letter in sender:
        if letter == '!':
            return sender[1:i]


def connect_to_channels(channels):
    # TODO: documentation
    '''

    '''


    # TODO: Add some randomized quotes.
    hello_msg = "Hello, world!"

    for channel in channels:
        s.send("JOIN %s\r\n" % channel)
        # s.send("PRIVMSG %s :%s\r\n" % (channel, hello_msg))


def get_tags(statement, command):
    # TODO: documentation
    '''
    '''


    tags = []

    for i, item in enumerate(command):
        if item == statement:
            tags.extend(command[i:])
            break

    if len(tags) > 1:
        tags = tags[1:]

    else:
        return []

    return tags


def get_command(mode, channel, command, sender):
    # TODO: documentation
    '''
    '''


    message = ""

    # TODO: check if command was directed from a channel(#) or from a PM
    if mode == 'PRIVMSG':
        print command
        if ':!uptime' in command:
            current_time = time.time() - time_at_start
            message = uptime(channel, current_time)

        elif ':!gif' in command:
            tags = get_tags(':!gif', command)
            message = gif(channel, tags)

    elif mode == 'KICK':
        msg = random.choice(quotes['kicked'])
        message = rejoin(channel, msg)

    # TODO: Add displaying current time
    # TODO: What to display?
    if message:
        print(">>> %s" % message[:-4])
        s.send(message)


def get_input(line):
    # TODO: documentation
    '''
    '''


    for i, item in enumerate(line):
        # TODO: make the bot understand commands
        # TODO: make the bot react to commands
        # TODO: trim the user that sends messages
        # TODO: format: date, mode, channel, sender, msg
        if item in modes:
            mode = item
            sender = line[i - 1]
            channel = line[i + 1]
            command = line[i:]
            get_command(mode, channel, command, sender)

        else:
            # TODO: What to display?
            print item + " | ",

    print ""


def main():
    # TODO: documentation
    '''

    '''


    # TODO: documentation
    setup()
    display_hello_message()

    connected = False
    readbuffer = ""


    while True:
        # TODO: documentation
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop( )

        # TODO: documentation
        for line in temp:
            line = string.rstrip(line)
            line = string.split(line)

            get_input(line)

            # TODO: documentation
            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
                if not connected:
                    connect_to_channels(channels)
                    connected = True


# run the main function
if __name__ == '__main__':
    main()
