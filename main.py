from __future__ import with_statement

import os
import jinja2
import webapp2
import logging
import urllib2
import random
import re
from time import localtime, strftime

from lib import meetup_api_client as mac

from secrets import MEETUP_API_KEY

template_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(),'templates')))

#myuser ='lucasrangit'
myid = 10705006

# QR code max 177x177 px and 4,296 alphanumeric characters.
qr_url = 'https://chart.googleapis.com/chart?cht=qr&choe=UTF-8&chs=150x150'

def remove_img_tags(data):
    p = re.compile(r'<img.*?>')
    return p.sub('', data)

class MainPage(webapp2.RequestHandler):

  def get(self):
    mucli = mac.Meetup(MEETUP_API_KEY)

    mygroups = mucli.get_groups(member_id=myid,text_format="plain")
    
    g = mygroups.results[random.randrange(0, mygroups.meta['total_count'])]
    logging.info("Group ID: " + str(g.id))
    logging.info(remove_img_tags(g.description))
    
    if g.get_events(mucli,status="upcoming").meta['count'] > 0:
      e = g.get_events(mucli,status="upcoming",text_format="plain").results[0]
      logging.info("Event ID: " + str(e.id))
      event_name = e.name
      event_datetime = strftime('%A %B %d', localtime(e.time/1000))
    else:
      event_name = ''
      event_datetime = ''
      
    if hasattr(g, 'group_photo'):
      group_photo_link = g.group_photo['photo_link']
    else:
      group_photo_link = 'http://img2.meetupstatic.com/03115515559398589850/img/user_logos/meetup_logo_1.png'
      #group_photo_link = '/static/keep-calm-and-meetup-dotcom.png'
    
    template = template_env.get_template('home.html')
    context = {
      'name': g.name,
      'link' : g.link,
      'photo_link' : group_photo_link,
      'qr_code' : qr_url + "&chl=" + g.link,
      'description' : remove_img_tags(g.description),
      'event_name' : event_name,
      'event_datetime' : event_datetime,
    }
    self.response.out.write(template.render(context))


application = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
