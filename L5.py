# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
from urllib import request
from functools import reduce

pickle_data_ulr = 'http://www.pythonchallenge.com/pc/def/banner.p'
result = request.urlopen(pickle_data_ulr)
unpickled_data = pickle.loads(result.read())

with open('pickle_translate.txt', 'a+') as pickle_translate:
    for array in unpickled_data:
        result_list = list(map(lambda set: set[0]*set[1] ,array))
        result_str = "".join(string for string in result_list)
        pickle_translate.write(result_str + '\n')
    pickle_translate.close()

# channel