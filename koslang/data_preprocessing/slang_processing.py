# Slang Processing
import pandas as pd

#go-ring
def ko_data(path):
    data = pd.read_csv(path,dtype={'': str,'prefix': int, 'suffix': int, 'interjection': int, 'fortis': int, 'idiom': int, 'abbreviation': int, 'long-phonetic': int, 'numNkor': int, 'engNkor': int, 'abstract': int, 'shape-shift': int, 'eroticism': int, 'specific': int}, names=['','prefix', 'suffix', 'interjection', 'fortis', 'idiom', 'abbreviation', 'long-phonetic', 'numNkor', 'engNkor', 'abstract', 'shape-shift', 'eroticism', 'specific'], sep=',', index_col=0)
    return data

#chaeha
def slang_TxtToDf(path):
    Df = pd.read_csv(path,dtype={'': str,'prefix': int, 'suffix': int, 'interjection': int, 'fortis': int, 'idiom': int, 'abbreviation': int, 'long-phonetic': int, 'numNkor': int, 'engNkor': int, 'abstract': int, 'shape-shift': int, 'eroticism': int, 'specific': int}, names=['','prefix', 'suffix', 'interjection', 'fortis', 'idiom', 'abbreviation', 'long-phonetic', 'numNkor', 'engNkor', 'abstract', 'shape-shift', 'eroticism', 'specific'], sep=',',index_col=0)
    return Df

def createDataset(path):
    dataset = pd.read_csv(path,
                     dtype={'': str,'prefix': int, 'suffix': int, 'interjection': int, 'fortis': int, 'idiom': int, 'abbreviation': int, 'long-phonetic': int, 'numNkor': int, 'engNkor': int, 'abstract': int, 'shape-shift': int, 'eroticism': int, 'specific': int},
                     names=['','prefix', 'suffix', 'interjection', 'fortis', 'idiom', 'abbreviation', 'long-phonetic', 'numNkor', 'engNkor', 'abstract', 'shape-shift', 'eroticism', 'specific'],
                     sep=',',
                     index_col=0)
    return dataset