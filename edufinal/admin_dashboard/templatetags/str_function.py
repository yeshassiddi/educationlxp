from django import template
register = template.Library()
from datetime import  timezone
from dateutil.tz import gettz

@register.filter
def date_exact(date_agi):
    return date_agi.strftime("%d %b %Y")


@register.filter
def date_exact_time(date_agi):
    return date_agi.strftime("%d %B %Y %H:%M:%S")


from datetime import date
import datetime


@register.filter
def MinuteHourAgo(time):

    '''Demonstrate docstring for informing that this Python View based function will give an exact time of message when this message was sent by user'''

    now = datetime.datetime.now(tz=gettz('Asia/Kolkata'))
    diff = now - time
    second_diff = diff.seconds
    day_diff = diff.days
    if day_diff < 0:
        return 'dss'

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(int(second_diff)) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(int(second_diff / 60)) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(int(second_diff / 3600)) + " hours ago"

    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(int(day_diff)) + " days ago"
    if day_diff < 31:
        return str(int(day_diff / 7)) + " weeks ago"
    if day_diff < 365:
        return str(int(day_diff / 30)) + " months ago"

    return str(day_diff / 365) + " years ago"
