#!/usr/bin/env python
# encoding: utf-8


# description
# TODO: documentation


# imports
import sys
import socket
import string
import time


# settings
s = socket.socket()
channels = ['#weezky', '#jhgrng']


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


    hello_msg = "Hello, world!"

    for channel in channels:
        s.send("JOIN %s\r\n" % channel)
        s.send("PRIVMSG %s :%s\r\n" % (channel, hello_msg))


def get_mode(mode):
    # TODO: documentation
    '''
    '''


    if mode == 'PRIVMSG':
        pass

    if mode == 'KICK':
        pass


def get_channel():
    # TODO: documentation
    '''
    '''


    pass


def main():
    # TODO: documentation
    '''

    '''


    # TODO: documentation
    setup()
    display_hello_message()
    time_at_start = time.time()

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

            # TODO: documentation
            for i in line:
                # TODO: make the bot understand commands
                # TODO: make the bot react to commands
                print i,

            print ""

            # TODO: documentation
            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
                if not connected:
                    connect_to_channels(channels)
                    connected = True


# run the main function
if __name__ == '__main__':
    main()
