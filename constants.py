"""
constants for the grind_txts module. require people to choose from a dropdown
instead of allowing them to input their own carrier. this way you can ensure
it maps correctly.
"""

CARRIER_MAP = {
    'alltel': 'message.alltel.com',
    'att': 'mms.att.net',
    'boost': 'myboostmobile.com',
    'nextel': 'messaging.nextel.com',
    'sprint': 'pm.sprint.com',
    'tmobile': 'tmomail.net',
    'uscellular': 'email.uscc.net',
    'verizon': 'vzwpix.com', # allows > 160 char messages to be sent as one msg
    'virgin': 'vmobl.com'
}

EMAIL_ADDR = 'gmail_username@gmail.com'
EMAIL_PASSWD = 'gmail_password'
EMAIL_USERNAME = 'gmail_username'
