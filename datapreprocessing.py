import pandas as pd
import os.path
# Load the Parquet file



def loadData():

    """
    Load the articles.parquet into a pandas

    :return: return a raw pandas dataframe
    """
    # we have to make sure the file is actually downloaded
    assert os.path.isfile("dataset/articles.parquet"), "No dataset in dataset/ folder"
      
    print("Loaded dataset succesfully:")
    rawDataFrame = pd.read_parquet('dataset/articles.parquet')
    return rawDataFrame


def filtherToReality(rawDataFrame):

    '''
     Filther to only have articles from entertainment
    :param rawDataFrame: Raw articles from eb-nerd

    :return: filthered pandas dataframe only containing reality
    '''
    entertainmentDF = rawDataFrame[rawDataFrame['category_str'] == 'underholdning']
    return entertainmentDF










