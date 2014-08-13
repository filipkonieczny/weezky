#!/usr/bin/env python
# encoding: utf-8


# description
# weezky - a Python IRC bot.
# Joins channels, listens and sometimes does something.
# You can find currently available commands in commands.py.


# imports
import socket
import string
import time
import json
import random

from commands import rejoin, uptime, gif, join, part, quote


# settings
s = socket.socket()
channels = ['#weezky']
modes = ['PRIVMSG', 'KICK']
time_at_start = time.time()


# quotes
quotes_file = open('quotes.json').read()
quotes = json.loads(quotes_file)


# functions
def setup():
    '''Establishes the connection. Simple as that.

    '''

    nick = "weezky"

    s.connect(('irc.quakenet.org', 6667))
    s.send("NICK %s\r\n" % nick)
    s.send("USER %s %s bla :%s\r\n" % (nick, nick, nick))


def connect_to_channels(channels):
    '''After pinging connect to predefined channels.

    ([strings]) -> socket.send()

    >>> connect_to_channels(['#weezky1', '#weezky2'])
    s.send('JOIN #weezky\r\n')
    s.send('JOIN #weezky\r\n')

    '''

    for channel in channels:
        s.send("JOIN %s\r\n" % channel)


def strip_sentence(statement, command):
    '''Strips a sentence to reveive only words.
    Also omits the command at the beginning of the sentence.

    (str) -> [strings]

    >>> strip_sentence(':!command This is a sentence.')
    ['this', 'is', 'a', 'sentence.']

    '''

    words = []

    for i, item in enumerate(command):
        if item == statement:
            words.extend(command[i:])
            break

    if len(words) > 1:
        words = words[1:]

    else:
        return []

    return words


def get_command(mode, channel, command):
    '''Decide what to do based on the user input.

    (str, str, [strings], str) -> socket.send()

    >>> get_command('PRIVMSG', '#weezky', ':!quote')
    socket.send('PRIVMSG #weezky :Houston, we have a problem.\r\n')

    '''

    message = ""

    if mode == 'PRIVMSG':
        print command
        if ':!uptime' in command:
            current_time = time.time() - time_at_start
            message = uptime(channel, current_time)

        elif ':!gif' in command:
            tags = strip_sentence(':!gif', command)
            message = gif(channel, tags)

        elif ':!join' in command:
            channels = strip_sentence(':!join', command)
            join(s, channels)

        elif ':!part' in command:
            channels = strip_sentence(':!part', command)
            part(s, channels)

        elif ':!quote' in command:
            msg = random.choice(quotes['quotes'])
            message = quote(channel, msg)

    elif mode == 'KICK':
        msg = random.choice(quotes['kicked'])
        message = rejoin(s, channel, msg)

    if message:
        print(">>> %s" % message[:-4])
        s.send(message)


def get_input(line):
    '''Analyzes every line that weezky receives.
    Sends the data further to get_command().

    ([strings]) -> [strings]

    >>> get_input(['this', 'is', 'a', 'line'])
    get_command()

    '''

    for i, item in enumerate(line):
        if item in modes:
            mode = item
            channel = line[i + 1]
            command = line[i:]
            get_command(mode, channel, command)

        else:
            print item + " | ",

    print ""


def main():
    '''Main function. Takes care of all the logic.
    Listens, reacts to commands, sometimes talks.
    Cool stuff!

    '''

    # establish the connection
    setup()

    readbuffer = ""

    while True:
        # listen to what's going on
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop( )

        # analyze what's going on
        for line in temp:
            line = string.rstrip(line)
            line = string.split(line)

            get_input(line)

            # ping pong!
            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
                connect_to_channels(channels)


# run the main function
if __name__ == '__main__':
    main()
