# http://www.pythonchallenge.com/pc/def/channel.jpg

from functools import reduce
from urllib import request
from L3 import get_text
from L2 import get_characters
from zipfile import ZipFile
from urllib import request

pickle_data_ulr = 'http://www.pythonchallenge.com/pc/def/banner.p'
result = request.urlopen(pickle_data_ulr).read()

with ZipFile('my_file.zip', 'w') as myzip:
    myzip.write(result)

pass