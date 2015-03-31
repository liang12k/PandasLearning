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
    elts=[s.text_content() for s in elts]
    elts=[" ".join(
            (s.replace("\n","")
              # .replace("\ue002","")
              # .replace("\ue004","")
              .encode("ascii","ignore")
            ).strip().split())
          for s in elts]
    return elts

print _unpack(rows[0],kind="th")
# ['Strike Filter', 'Contract Name', 'Last', 'Bid', 'Ask', 'Change', '%Change', 'Volume', 'Open Interest', 'Implied Volatility']
print _unpack(rows[1],kind="td") # [['modify']]
print _unpack(rows[2],kind="td")
# ['90.00', 'AAPL150402P00090000', '0.01', '0.00', '0.01', '0.00', '0.00%', '888', '1008', '125.00%']

# # converting data set into DataFrame
# # **note: not all cols to be converted
# #         to floating point format
def parse_options_data(table):
    """ using pd.io.parsers.TextParser """
    rows=table.findall(".//tr")
    header = _unpack(rows[0],kind="th")
    data=[_unpack(r) for r in rows[2:]]
    return pd.io.parsers.TextParser(
               data,names=header
           ).get_chunk()

call_data=parse_options_data(calls)
print call_data[-10:].ix[:,["Strike","Change","Last","Bid","Ask","Contract Name"]]
'''
    Strike  Change   Last    Bid    Ask        Contract Name
28     NaN   -2.95   5.90   5.60   5.75  AAPL150402P00132000
29     NaN   -2.42   7.41   6.60   6.80  AAPL150402P00133000
30     NaN   -1.98   8.72   7.55   7.80  AAPL150402P00134000
31     NaN    0.00  11.53   8.60   8.80  AAPL150402P00135000
32     NaN    0.00  12.55   9.60   9.80  AAPL150402P00136000
33     NaN    0.00  11.92  10.55  10.80  AAPL150402P00137000
34     NaN    0.00  10.87  11.55  11.80  AAPL150402P00138000
35     NaN   -1.85  14.55  13.55  13.80  AAPL150402P00140000
36     NaN    0.00  17.85  18.55  18.80  AAPL150402P00145000
37     NaN    0.00  26.40  23.55  23.80  AAPL150402P00150000
'''
put_data =parse_options_data(puts)
print put_data[-10:].ix[:,["Strike","Change","Last","Bid","Ask","Contract Name"]]
'''
    Strike  Change  Last  Bid   Ask        Contract Name
32     NaN   -0.01  0.01    0  0.01  AAPL150402C00138000
33     NaN    0.00  0.01    0  0.01  AAPL150402C00139000
34     NaN    0.00  0.01    0  0.01  AAPL150402C00140000
35     NaN    0.00  0.01    0  0.01  AAPL150402C00141000
36     NaN    0.00  0.01    0  0.01  AAPL150402C00142000
37     NaN    0.00  0.01    0  0.01  AAPL150402C00143000
38     NaN    0.00  0.01    0  0.01  AAPL150402C00145000
39     NaN    0.00  0.02    0  0.01  AAPL150402C00146000
40     NaN    0.00  0.01    0  0.01  AAPL150402C00150000
41     NaN    0.00  0.01    0  0.01  AAPL150402C00155000
'''
