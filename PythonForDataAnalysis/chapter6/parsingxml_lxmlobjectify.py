"""
XML: (extensible markup language)
-one of the common structured data format
 supporting hierarchical, nested data
 with metadata
"""

import lxml
import pandas as pd
from StringIO import StringIO

'''
MTA: NY Metropolitan Transportation Authority
-data series about bus, train services

Investigate:
look at performance data contained in a set of
XML files.
each train, bus service has different file
containing monthly data as series of XML
records
'''

# created this sample file based on the pdf's
# sample .xml text
path="Performance_MNR_example.xml"
parsed=lxml.objectify.parse(open(path))
root=parsed.getroot()
root
# <Element INDICATOR at 0x10263d248>
data=[]
skip_fields=[
    "PARENT_SEQ","INDICATOR_SEQ",
    "DESIRED_CHANGE","DECIMAL_PLACES"
]
for elt in root:
    el_data={}
    for child in elt.getchildren():
        if child.tag in skip_fields: continue
        el_data[child.tag]=child.pyval
    data.append(el_data)

perf=pd.DataFrame(data); print perf.T
'''
                                                                0
AGENCY_NAME                                  Metro-North Railroad
CATEGORY                                       Service Indicators
DESCRIPTION     Percent of the time that escalators are operat...
FREQUENCY                                                       M
INDICATOR_NAME                             Escalator Availability
INDICATOR_UNIT                                                  %
MONTHLY_ACTUAL
MONTHLY_TARGET                                                 97
PERIOD_MONTH                                                   12
PERIOD_YEAR                                                  2011
YTD_ACTUAL
YTD_TARGET                                                     97
'''

# # **note: XML data can get more complicated
# # -each tag can have its own metadata
#
# ex: HTML link tag is a valid XML
tag="<a href='http://www.google.com'>Google</a>"
root=(lxml.objectify
          .parse(StringIO(tag)
    ).getroot())
root
# <Element a at 0x104a1f320>
print root.get("href")
# 'http://www.google.com'
print root.text
# 'Google'
