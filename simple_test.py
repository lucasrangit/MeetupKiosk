#!/usr/bin/env python

# http://www.meetup.com/meetup_api/console/?path=/2/members
# https://github.com/davemosk/python-api-client/wiki for API call examples
# https://github.com/omwah/python-api-client for the fork with API v2 support
# https://developers.google.com/chart/infographics/docs/qr_codes QR code image

# TODO display date and time of event

from __future__ import with_statement
from lib import meetup_api_client as mac

import urllib2
from time import localtime, strftime

import secret

#myuser ='lucasrangit'
myid = 10705006

# QR code max 177x177 px and 4,296 alphanumeric characters.
qr_url = 'https://chart.googleapis.com/chart?cht=qr&choe=UTF-8&chs=150x150'

mucli = mac.Meetup(secret.MEETUP_API_KEY)

mygroups = mucli.get_groups(member_id=myid)

for g in mygroups.results:
  print "ID:", g.id
  print g.name
  print g.group_photo['photo_link']
  print g.link
  print "QR code:", qr_url + "&chl=" + g.link
  print g.description[:80], "..."
  print "Upcoming events:", g.get_events(mucli,status="upcoming",text_format="simplehtml").meta['count']
  for e in g.get_events(mucli,status="upcoming").results:
    print "ID:", e.id
    print strftime('%Y-%m-%d %H:%M:%S', localtime(e.time/1000))
    print e.description[:80], "..."
    print 
    break
  break
