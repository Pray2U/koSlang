# koSlang/koslang/modules.py
from data_preprocessing import slang_processing
from konlpy.tag import Kkma
from eunjeon import Mecab
from konlpy.tag import Okt

class koslang():
    def isSlang(self, sentence:str):
        '''

        :param sentence: Sentence with unspecified content.
        :return: Returns "True" if profanity is included, "False" otherwise.

        kkma.morphs()
        mecab.nouns()
        okt.phrases()

        Explain to our algorithm.
        1. Import dataframe
        2. Parameter Sentence is divided into test cases using the following three functions.
            - kkma.morphs()
            - mecab.nouns()
            - okt.phrases()
        3. Check the test cases divided according to each case belong to the DataFrame one by one.
        4. If at least one case is included, we return "True" value, otherwise return "False" value.

        ▼ Write your Code ▼
        '''
        kkma = Kkma()
        okt = Okt()
        mecab = Mecab()

        slang_df = slang_processing.slang_TxtToDf('./data_preprocessing/slang_text.txt')

        mo = kkma.morphs(sentence)
        phr = okt.phrases(sentence)
        noun = mecab.nouns(sentence)

        for slang in slang_df.index:
            if slang in mo or slang in noun or slang in phr:
                return True

        return False


if __name__ == "__main__":
    koslang = koslang()
    exp = input("Input test sentence")
    print(koslang.isSlang(exp))


