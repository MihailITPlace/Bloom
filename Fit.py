import os
import re

from BloomFilter import BloomFilter

path = 'texts_eng/'
path_f = 'filters_en/'

texts = os.listdir(path)

for i in texts:
    with open(path + i, 'rb') as f:
        bf = BloomFilter(10000)
        lines = list(f)
        for l in lines:
            s = l.decode("utf-8")
            s = re.sub('[^A-Za-z0-9 ]+', '', s)
            bf.fit(s.split(' '))
        bf.save(path_f + i)