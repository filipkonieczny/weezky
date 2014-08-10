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

from commands import rejoin, uptime


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


def connect_to_channels(channels):
    # TODO: documentation
    '''

    '''


    # TODO: Add some randomized quotes.
    hello_msg = "Hello, world!"

    for channel in channels:
        s.send("JOIN %s\r\n" % channel)
        s.send("PRIVMSG %s :%s\r\n" % (channel, hello_msg))


def get_command(mode, channel, command):
    # TODO: documentation
    '''
    '''


    # TODO: check if command was directed from a channel(#) or from a PM
    if mode == 'PRIVMSG':
        print command

        if '!uptime' in command:
            current_time = time.time() - time_at_start
            uptime(s, channel, current_time)

    elif mode == 'KICK':
        msg = random.choice(quotes['kicked'])
        print msg
        rejoin(s, channel, msg)


def get_input(line):
    # TODO: documentation
    '''
    '''


    for i, item in enumerate(line):
        # TODO: make the bot understand commands
        # TODO: make the bot react to commands
        if item in modes:
            mode = item
            channel = line[i + 1]
            command = line[i + 2]
            get_command(mode, channel, command)

        # TODO: Add displaying current time, like in every IRC client
        print item,

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
