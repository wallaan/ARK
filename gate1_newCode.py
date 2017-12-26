import itertools
from itertools import product
import string
import urllib
import configparser


digits = string.digits

andrew_group = itertools.product(digits, repeat=1)
rob_group = itertools.product(digits, repeat=1)
koy_group = itertools.product(digits, repeat=1)


for prod in itertools.product(andrew_group, rob_group, koy_group):
    string = ''.join([''.join(k) for k in prod])
    print(string + '\n')




