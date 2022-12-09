# Slang Processing
import pandas as pd

#go-ring
def ko_data(path):
    data = pd.read_csv(path, names=['prefix', 'suffix', 'interjection', 'fortis', 'idiom', 'abbreviation', 'long-phonetic', 'numNkor', 'engNkor', 'abstract', 'shape-shift', 'eroticism', 'specific'], sep=',')
    return data

#chaeha
def slang_TxtToDf(path):
    Df = pd.read_csv(path, names=['','prefix', 'suffix', 'interjection', 'fortis', 'idiom', 'abbreviation', 'long-phonetic', 'numNkor', 'engNkor', 'abstract', 'shape-shift', 'eroticism', 'specific'], sep=',',index_col=0)
    return Df