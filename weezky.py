#!/usr/bin/env python
# encoding: utf-8


# description


# imports
import sys
import socket
import string


# settings
s = socket.socket()


# functions
def setup():
    '''

    '''


    host = "irc.quakenet.net"
    port = 6667
    nick = "weezky"
    ident = "weezky"
    realname = "weezky"

    s.connect(('irc.quakenet.org', 6667))
    s.send("NICK %s\r\n" % nick)
    s.send("USER %s %s bla :%s\r\n" % (ident, host, realname))


def display_hello_message():
    '''
    '''


    print("\nHello!\n\n\n")


def main():
    '''

    '''


    setup()
    display_hello_message()

    readbuffer = "" 


    while True:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop( )

        for line in temp:
            line = string.rstrip(line)
            line = string.split(line)

            for i in line:
                print i,

            print ""

            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
                s.send("JOIN #weezky\r\n")
                s.send("PRIVMSG #weezky %s\r\n" % ("Yo!"))


# run the main function
if __name__ == '__main__':
    main()