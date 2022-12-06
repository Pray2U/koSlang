# Slang Processing
import pandas as pd

#go-ring
def ko_data():
    data = pd.read_csv('koslang_last.txt', names=['prefix', 'suffix', 'interjection', 'fortis', 'idiom', 'abbreviation', 'long-phonetic', 'numNkor', 'engNkor', 'abstract', 'shape-shift', 'eroticism', 'specific'], sep=',')
    return data
