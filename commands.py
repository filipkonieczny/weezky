#!/usr/bin/env python
# encoding: utf-8


# description
# commands module that contains all commands that weezky reacts to:
# !rejoin - rejoin a channel after being kicked, say something
# !uptime - get info about the uptime
# !gif <tag(s)> - get a gif with given tag(s)
# !join <channel(s)> - join given channel(s)
# !part <channel(s)> - part given channel(s)
# !quote - get a random quote from quotes.json


# imports
import urllib, json


# functions
def rejoin(socket, channel, msg=""):
    '''Rejoin a channel after being kicked and say something.

    (socket, str, str) -> str

    >>> rejoin(s, '#weezky', 'Dude, where's my car?!')
    'PRIVMSG #weezky :Dude, where\'s my car?!\r\n'

    '''

    socket.send('JOIN %s\r\n' % channel)

    if msg:
        return 'PRIVMSG %s :%s\r\n' % (channel, msg)


def format_time(time):
    '''Get number of seconds from time.time() and format it nicely.
    Takes a float, returns a dict with formatted time.

    (float) -> dict

    >>> format_time(86461.0)
    {'days': 1, 'hours': 0, 'minutes': 1, 'seconds': 1}

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
    '''Returns a message with current uptime.
    Uses 'format_time()' function to easily convert float to dict.

    (str, float) -> str

    >>> uptime('#weezky', 86461.0)
    'PRIVMSG #weezky :Current uptime: 1 days, 0 hours, 1 minutes and 1 seconds.\r\n'

    '''

    uptime = format_time(uptime)
    msg = "Current uptime: %s days, %s hours, %s minutes and %s seconds." % (uptime['days'],
                                                                             uptime['hours'],
                                                                             uptime['minutes'],
                                                                             uptime['seconds'])

    return 'PRIVMSG %s :%s\r\n' % (channel, msg)


def gif(channel, tags):
    '''Collects a gif with given tag(s).

    ([list of strings]) -> str

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

    # if there is no such gif
    if len(data["data"]) == 0:
        return 'PRIVMSG %s :%s\r\n' % (channel, "No such gif!")

    # return the link to a randomly selected gif(taking into account tags)
    data = data["data"]["image_original_url"]
    return 'PRIVMSG %s :%s\r\n' % (channel, data)


def join(s, channels):
    '''Join channel(s).

    (socket, [list of strings]) -> socket.send()

    >>> join(s, ['#weezky1', '#weezky2'])
    s.send('JOIN #weezky1\r\n')
    s.send('JOIN #weezky2\r\n')

    '''

    for i in channels:
        s.send('JOIN %s\r\n' % i)


def part(s, channels):
    '''Part(leave) channel(s).

    (socket, [list of strings]) -> socket.send()

    >>> leave(s, ['#weezky1', '#weezky2'])
    s.send('PART #weezky1\r\n')
    s.send('PART #weezky2\r\n')

    '''

    for i in channels:
        s.send('PART %s\r\n' % i)


def quote(channel, msg):
    '''Display a random quote from quotes.json.

    (str, str) -> str

    >>> quote('#weezky', 'Are we there yet?')
    'PRIVMSG #weezky :Are we there yet?\r\n'

    '''

    return 'PRIVMSG %s :%s\r\n' % (channel, msg)
