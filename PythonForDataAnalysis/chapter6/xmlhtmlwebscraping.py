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
# <lxml.etree._ElementTree at 0x10496c200>

doc=parsed.getroot(); doc
# <Element html at 0x104414838>
links=doc.findall(".//a"); links[15:20]
# objs represent html elements
'''
[<Element a at 0x104963f18>,
 <Element a at 0x104963f70>,
 <Element a at 0x104963fc8>,
 <Element a at 0x104977050>,
 <Element a at 0x1049770a8>]
'''
# get the url
lnk=links[28]
# # sample: getting 'href'
lnk.get("href") # 'https://autos.yahoo.com/'
lnk.text_content() # 'Autos'
# # list comprehension to get all urls
urls=[lnk.get("href") for lnk in doc.findall(".//a")]
urls[:10 ]
'''
['https://www.yahoo.com/',
 'https://mail.yahoo.com/?.intl=us&.lang=en-US&.src=ym',
 'https://search.yahoo.com/search',
 'http://news.yahoo.com/',
 'http://sports.yahoo.com/',
 'http://finance.yahoo.com/',
 'https://weather.yahoo.com/',
 'https://games.yahoo.com/',
 'https://answers.yahoo.com/',
 'https://screen.yahoo.com/']
'''
urls[-10:]
'''
['/q/op?s=AAPL&strike=137.00',
 '/q?s=AAPL150402P00137000',
 '/q/op?s=AAPL&strike=138.00',
 '/q?s=AAPL150402P00138000',
 '/q/op?s=AAPL&strike=140.00',
 '/q?s=AAPL150402P00140000',
 '/q/op?s=AAPL&strike=145.00',
 '/q?s=AAPL150402P00145000',
 '/q/op?s=AAPL&strike=150.00',
 '/q?s=AAPL150402P00150000']
'''
# # **note:
# # finding right tables may take trial & error
tables=doc.findall(".//table")
'''
[<Element table at 0x1066be2b8>,
 <Element table at 0x1066be310>,
 <Element table at 0x1066be368>]
'''
calls=tables[-1]; print calls
# <Element table at 0x106918c00>
puts=tables[1];   print puts
# <Element table at 0x106918ba8>
rows=calls.findall(".//tr")
# # get header row
print len(rows) # 40

def _unpack(row,kind="td"):
    """ extract text from each header, row """
    elts=row.findall(".//%s" % kind)
    # elts=[s.text_content() for s in elts]
    # elts=[s for s in elts if s.strip()]
    return [val.text_content() for val in elts]

print _unpack(rows[0],kind="th")
# 
