# hada example d module n9dro n import d code wa7d 5ore 
# dir ghir from validator import validate_email

import re


def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))


