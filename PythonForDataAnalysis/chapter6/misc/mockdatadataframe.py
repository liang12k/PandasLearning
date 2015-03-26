"""
put all mock data google, twitter into dataframe
"""
import  googleplus_mockdata as googledata
import twitter_mockdata as twitterdata
import pandas as pd

googleDf=pd.DataFrame(
    [googledata.activity0,
     googledata.activity1,
     googledata.activity2,
     googledata.activity3]
)
googleDf

twitterDf=pd.DataFrame(
    [twitterdata.status0,
     twitterdata.status1,
     twitterdata.status2]
)
twitterDf
