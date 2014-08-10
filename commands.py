#!/usr/bin/env python
# encoding: utf-8


# description


# imports


# settings


# functions
def rejoin(socket, channel, msg=""):
    # TODO: documentation
    '''
    '''


    s = socket

    s.send('JOIN %s\r\n' % channel)

    if msg:
        s.send('PRIVMSG %s :%s\r\n' % (channel, msg))
