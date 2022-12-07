# Slang Processing
import pandas as pd

#go-ring
def ko_data():
    data = pd.read_csv('koslang_last.txt', names=['prefix', 'suffix', 'interjection', 'fortis', 'idiom', 'abbreviation', 'long-phonetic', 'numNkor', 'engNkor', 'abstract', 'shape-shift', 'eroticism', 'specific'], sep=',')
    return data

#chaeha
def slang_TxtToDf():
    Df = pd.read_csv('slang_text.txt', names=['','prefix', 'suffix', 'interjection', 'fortis', 'idiom', 'abbreviation', 'long-phonetic', 'numNkor', 'engNkor', 'abstract', 'shape-shift', 'eroticism', 'specific'], sep=',',index_col=0)
    return Df
