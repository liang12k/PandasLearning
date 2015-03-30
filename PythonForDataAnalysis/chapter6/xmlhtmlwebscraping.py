"""
lxml: parsing large files
-html: lxml.html
-xml:  lxml.objectify
"""

import pandas as pd
from lxml.html import parse
from urllib2 import urlopen

'''
Yahoo! Finance stock options data
-options: 
 derivative contracts giving user the right to:
 >buy:  call option
 >sell: put  option
 a company's stock at a particular price (strike)
 between now and in the future (expiry).

: people trade both call,put options across many
  strikes and expires
'''

parsed=parse(
    urlopen("http://finance.yahoo.com/q/op?s=AAPL+Options")
)
doc=parsed.getroot(); doc

links=doc.findall(".//a"); links[15:20]

