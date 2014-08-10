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
        return 'PRIVMSG %s :%s\r\n' % (channel, msg)


def format_time(time):
    # TODO: documentation
    '''
    '''

    uptime = {}

    seconds_in_day = 60 * 60 * 24 * 1.0
    seconds_in_hour = 60 * 60 * 1.0
    seconds_in_minute = 60 * 1.0

    days = int(time / seconds_in_day)
    uptime['days'] = days
    time -= days * seconds_in_day

    hours = int(time / seconds_in_hour)
    uptime['hours'] = hours
    time -= hours * seconds_in_hour

    minutes = int(time / seconds_in_minute)
    uptime['minutes'] = minutes
    time -= minutes * seconds_in_minute

    uptime['seconds'] = int(time)

    return uptime


def uptime(socket, channel, uptime):
    # TODO: documentation
    '''
    '''


    s = socket

    uptime = format_time(uptime)
    msg = "Current uptime: %s days, %s hours, %s minutes and %s seconds." % (uptime['days'],
                                                                             uptime['hours'],
                                                                             uptime['minutes'],
                                                                             uptime['seconds'])

    return 'PRIVMSG %s :%s\r\n' % (channel, msg)
