# koSlang/koslang/koslang.py
from eunjeon import Mecab
import pandas as pd

def isSlang(sentence:str):
    '''
    :param sentence: Sentence with unspecified content.
    :return: Returns "True" if profanity is included, "False" otherwise.

    mecab.nouns()

    Explain to our algorithm.
    1. Import dataframe
    2. Parameter Sentence is divided into test cases using the following three functions.
        - kkma.morphs()
        - mecab.nouns()
        - okt.phrases()
    3. Check the test cases divided according to each case belong to the DataFrame one by one.
    4. If at least one case is included, we return "True" value, otherwise return "False" value.
    '''

    dataset = pd.read_csv("data.csv", sep=',', encoding='cp949', index_col=0)
    mecab = Mecab()
    noun = mecab.morphs(sentence)

    for slang in dataset.index:
        if slang in noun:
            return True
    return False

if __name__=="__main__":
     print(isSlang("이게 왜 안되는데"))