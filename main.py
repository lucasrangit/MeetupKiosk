# http://www.meetup.com/meetup_api/console/?path=/2/members
# https://github.com/davemosk/python-api-client/wiki for API call examples
# https://github.com/omwah/python-api-client for the fork with API v2 support
# https://developers.google.com/chart/infographics/docs/qr_codes QR code image

# TODO display date and time of event

from __future__ import with_statement

import os
import jinja2
import webapp2
import logging

from lib import meetup_api_client as mac

import urllib2
from time import localtime, strftime

from secrets import MEETUP_API_KEY

template_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(),'templates')))

#myuser ='lucasrangit'
myid = 10705006

# QR code max 177x177 px and 4,296 alphanumeric characters.
qr_url = 'https://chart.googleapis.com/chart?cht=qr&choe=UTF-8&chs=150x150'

class MainPage(webapp2.RequestHandler):

  def get(self):
    mucli = mac.Meetup(MEETUP_API_KEY)

    mygroups = mucli.get_groups(member_id=myid)

    g = mygroups.results[0]
    logging.info("Name: " + str(g.name))
    
    template = template_env.get_template('home.html')
    context = {
      'name': g.name,
      'link' : g.link,
    }
    self.response.out.write(template.render(context))

    return
    for g in mygroups.results:
      self.response.write("ID: " + str(g.id))
      self.response.write(g.name)
      self.response.write(g.group_photo['photo_link'])
      self.response.write(g.link)
      self.response.write("QR code: " + qr_url + "&chl=" + g.link)
      self.response.write(g.description[:80] + "...")
      self.response.write("Upcoming events: " + str(g.get_events(mucli,status="upcoming",text_format="simplehtml").meta['count']))
      for e in g.get_events(mucli,status="upcoming").results:
        self.response.write("ID: " + str(e.id))
        self.response.write(strftime('%Y-%m-%d %H:%M:%S', localtime(e.time/1000)))
        self.response.write(e.description[:80] + "...")
        break # stop on the first event
      break # stop on the first group


application = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
