MeetupKiosk
===========

Meetup.com Kiosk using the Python API running on Google App Engine. 

For the Southern California Linux Expo (SCaLE) Expo local LA Meetup booth, I put together a website that will cycle through the local Meetups that I am a member of. http://meetupkiosk.appspot.com/ displays the most basic data for now and a QR code for people to sign up. I plan on setting up a Raspberry Pi and a monitor at the booth. 

Does someone want to help me improve this site? The app using my API key to access the Meetup.com API.

TODO
====

* Create CSS that mimic Meetup.com
* Cache the QR code image and save to static/ folder to save bandwidth
* Make refresh rate variable via a GET parameter
* Put Meetup description in a fixed size text box

References
==========

* http://www.meetup.com/meetup_api/console/?path=/2/members
* https://github.com/davemosk/python-api-client/wiki for API call examples
* https://github.com/omwah/python-api-client for the fork with API v2 support
* https://developers.google.com/chart/infographics/docs/qr_codes QR code image

