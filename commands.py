#!/usr/bin/env python
# encoding: utf-8


# description


# imports
import urllib, json


# settings


# functions
def rejoin(socket, channel, msg=""):
    # TODO: documentation
    '''
    '''

    socket.send('JOIN %s\r\n' % channel)

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


def uptime(channel, uptime):
    # TODO: documentation
    '''
    '''


    uptime = format_time(uptime)
    msg = "Current uptime: %s days, %s hours, %s minutes and %s seconds." % (uptime['days'],
                                                                             uptime['hours'],
                                                                             uptime['minutes'],
                                                                             uptime['seconds'])

    return 'PRIVMSG %s :%s\r\n' % (channel, msg)


def gif(channel, tags):
    # TODO: documentation
    '''This function collects a gif with a given tag(s).

    ([list of strings]) -> url


    >>> get_gif()
    "No tags given!"

    >>> get_gif([])
    "No tags given!"

    >>> get_gif(["asdfhaskljdbfhakljfaksdjfk"])
    "No such gif!"

    >>> get_gif(["funny", "cat"])
    "http://s3.amazonaws.com/giphymedia/media/6Hd1S34yv25UY/giphy.gif"

    '''


    # corner case - if there are no tags
    if len(tags) == 0:
        return 'PRIVMSG %s :%s\r\n' % (channel, "There are no tags!")


    print "tags:", tags

    # generate a search url for the image with given tags
    url_destination = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="

    for i, tag in enumerate(tags):
        url_destination += str(tag)

        # if there are more tags add a '+' to the url
        if i < len(tags) - 1:
            url_destination += "+"


    # load data for given url destination
    data = json.loads(urllib.urlopen(url_destination).read())

    print "data: ", data

    # if there is no such gif
    if len(data["data"]) == 0:
        return 'PRIVMSG %s :%s\r\n' % (channel, "No such gif!")


    # return the link to a randomly selected gif(taking into account tags)
    # print json.dumps(data, sort_keys=True, indent=4)
    data = data["data"]["image_original_url"]

    return 'PRIVMSG %s :%s\r\n' % (channel, data)


def join(s, channels):
    # TODO: documentation
    # TODO: check if user is already there, if is then:
    # TODO: display something like: "I'm already there, silly!"
    '''
    '''


    for i in channels:
        s.send('JOIN %s\r\n' % i)


def part(s, channels):
    # TODO: documentation
    '''
    '''


    for i in channels:
        s.send('PART %s\r\n' % i)


def quote(channel, msg):
    # TODO: documentation
    '''
    '''


    return 'PRIVMSG %s :%s\r\n' % (channel, msg)
