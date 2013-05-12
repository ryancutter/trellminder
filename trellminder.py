#!/usr/bin/python

"""
trellminder.py
~~~~~~~~~~~~~~

https://github.com/ryancutter/trellminder or https://ryancutter.org

This is the main (and only) module for the trellminder app.
"""

from sys import argv, exit
from getopt import getopt, GetoptError
from requests import get
from string import join
from datetime import datetime, date, timedelta
import smtplib, ConfigParser

def usage():
    """Print usage."""

    print "usage:"
    print "  -c config_file"

def getConfig(config_file, options):
    """Parse a config file for necessary parameters.

    Returns tuple of (key, token, email) strings.
    """

    config = ConfigParser.RawConfigParser()
    config.read(config_file)

    # read config params into a list
    vals = []
    for option in options: vals.append(config.get('Main', option))

    return tuple(vals)

def createLine(card, due_date):
    """Construct and return a string containing important info for a single card."""

    return "%s: %s\n%s\n\n" % (card['name'], due_date.strftime('%m-%d-%y'), card['shortUrl'])

def checkCards(cards):
    """Walk through all cards assigned to a particular user looking for ones
    which are overdue or due within the next day.

    Returns a tuple of (upcoming, overdue) strings.
    """
 
    now = date.today()
    tomorrow = now + timedelta(days=1) 

    upcoming, overdue = '', ''

    # parse cards looking for ones which are overdue or upcoming
    for card in cards:
        due_time = datetime.strptime(card['due'], '%Y-%m-%dT%H:%M:%S.%fZ')
        # don't care to consider H:M:S of due date, let's just focus on the day   
        due_date = date(due_time.year, due_time.month, due_time.day)

        if now > due_date:
            overdue += createLine(card, due_date)
        elif tomorrow >= due_date:
            upcoming += createLine(card, due_date)

    return upcoming, overdue

def sendEmail(email, mess):
    """Send email to interested parties."""

    body = join(("From: Trellminder",
                 "To: Users <noreply@rhcloud.com>",
                 "Subject: Trellminder Alert",
                 "",
                 mess), "\r\n")
    s = smtplib.SMTP('localhost')
    s.sendmail('noreply@rhcloud.com', [email], body)
    s.quit()

def main():
    """Main function."""

    # parse args
    try:
      opts, args = getopt(argv[1:], "c:", ["help"])
    except GetoptError, err:
      print str(err)
      usage()
      exit(2)

    for o, a in opts:
      if o == "-c":
        config_file = a
      else:
        assert False, "unhandled option" 

    # get config params
    key, token, email = getConfig(config_file, ('key', 'token', 'email'))

    # grab user data and parse it
    url = 'https://trello.com/1/members/my/cards?key=%s&token=%s' % (key, token) 
    upcoming, overdue = checkCards(get(url).json())

    # send email if necessary
    if overdue != '' or upcoming != '':
        # pretty up message a little
        if overdue == '': overdue = 'None\n'
        if upcoming == '': upcoming = 'None\n'
        mess = 'OVERDUE\n' + overdue + '\nUPCOMING\n' + upcoming
     
        sendEmail(email, mess)
 

if __name__ == "__main__":
    main()
