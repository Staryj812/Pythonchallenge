# http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib import request
import re

BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
REGEX = re.compile(r"next nothing is ([0-9]+)")

nothing = 16044/2 # initial nothing was 12345
while nothing:
    requestNothing = request.urlopen(BASE_URL + str(nothing))
    response = str(requestNothing.read())
    print(response)

    regex_match = re.search(REGEX, response)
    if regex_match and regex_match.group(1):
        nothing = regex_match.group(1)
    else:
        nothing = None
        break

# peak