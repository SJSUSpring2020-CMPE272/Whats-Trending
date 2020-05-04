import pandas as pd

def getCountryData(country):
    if (country == "US"):
        return pd.read_csv("usa_trending_videos.csv")
    elif (country == "CA"):
        return pd.read_csv("./transformed/CA_trending_videos.csv")
    elif (country == "UK"):
        return pd.read_csv("./transformed/GB_trending_videos.csv")
    elif (country == "FR"):
        return pd.read_csv("./transformed/FR_trending_videos.csv")
    elif (country == "DE"):
        return pd.read_csv("./transformed/DE_trending_videos.csv")
    elif (country == "MX"):
        return pd.read_csv("./transformed/MX_trending_videos.csv")


def getCategoryDesc(country):
    description = ''
    if (country == "US"):
        description = 'Videos of category Entertainment are the most trending in United States'
    elif (country == "CA"):
        description = 'Videos of category Entertainment are the most trending in Canada'
    elif (country == "UK"):
        description = 'Videos of category Music are the most trending in United Kingdom'
    elif (country == "FR"):
        description = 'Videos of category Entertainment are the most trending in France'
    elif (country == "DE"):
        description = 'Videos of category Entertainment are the most trending in Germany'
    elif (country == "MX"):
        description = 'Videos of category Entertainment are the most trending in Mexico'
    return description


def getPublishHour(country):
    description = ''
    if (country == "US"):
        description = 'Majority of the trending videos have been published at 3:00PM in United States'
    elif (country == "CA"):
        description = 'Majority of the trending videos have been published at 4:00PM in Canada'
    elif (country == "UK"):
        description = 'Majority of the trending videos have been published at 5:00PM in United Kingdom'
    elif (country == "FR"):
        description = 'Majority of the trending videos have been published at 4:00PM in France'
    elif (country == "DE"):
        description = 'Majority of the trending videos have been published at 5:00PM in Germany'
    elif (country == "MX"):
        description = 'Majority of the trending videos have been published at 2:00AM in Mexico'
    return description


def getTagCounts(country):
    description = ''
    if (country == "US"):
        description = 'The relation between number of tags in the video versus its trending level'
    return description


