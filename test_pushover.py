#!/home/cabox/.pyenv/versions/3.7.0/bin/python

from pushover_complete import PushoverAPI
from iperfspeed_config import *

p = PushoverAPI(p_apptoken)  # an instance of the PushoverAPI representing your application
p.send_message(p_userkey, 'PushoverAPI test')  # send a message to a user

