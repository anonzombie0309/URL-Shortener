import random
import string
import re

def generate_short_code(length=6):
    """Generate a random string of letters and digits."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def validate_url(url):
    """Simple URL validation using regex."""
    regex = re.compile(
        r'^(https?://)'                            # http or https
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6}'       # domain name
        r'|'                                       # OR
        r'localhost'                               # localhost
        r'|'                                       # OR
        r'\d{1,3}(\.\d{1,3}){3})'                  # IP address
        r'(:\d+)?'                                 # optional port
        r'(\/\S*)?$',                              # optional path
        re.IGNORECASE)
    return re.match(regex, url) is not None
