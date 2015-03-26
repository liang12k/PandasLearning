"""
put all mock data google, twitter into dataframe
"""
import  googleplus_mockdata as googledata
import twitter_mockdata as twitterdata
import pandas as pd

def getMockDataVariables(inpModule):
    """
        :return list: list of module's attributes (variable) values
    """
    return [
        getattr(inpModule,data)
        for data in dir(inpModule)
        if ("__" not in data
            and isinstance(
                    getattr(inpModule,data), dict)
        ) # end if
    ]

googleDf=pd.DataFrame(
    getMockDataVariables(googledata)
)
googleDf

twitterDf=pd.DataFrame(
    getMockDataVariables(twitterdata)
)
twitterDf
