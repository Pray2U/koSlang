# koSlang/koslang/modules.py
import time
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
        '''
        kkma = Kkma()
        okt = Okt()
        mecab = Mecab()

        slang_df = slang_processing.createDataset('./data_preprocessing/dataset.txt')

        # importingStartTime = time.time()
        # kkmaStartTime = time.time()
        mo = kkma.morphs(sentence)
        # kkmaEndTime = time.time()
        # print(f"kkma : {mo}")
        # oktStartTime = time.time()
        phr = okt.phrases(sentence)
        # oktEndTime = time.time()
        # print(f"okt : {phr}")
        # mecabStartTime = time.time()
        noun = mecab.morphs(sentence)
        # mecabEndTime = time.time()
        # print(f"mecab : {noun}")
        # importingEndTime = time.time()
        # print(f"All of Importing and Processing : {importingEndTime - importingStartTime:.5f}sec")
        # print(f"Kkma Processing : {kkmaEndTime - kkmaStartTime:.5f}sec")
        # print(f"Okt Processing : {oktEndTime - oktStartTime:.5f}sec")
        # print(f"Mecab Processing : {mecabEndTime - mecabStartTime:.5f}sec")
        #
        # travelsaryStartTime = time.time()
        for slang in slang_df.index:
            if slang in mo or slang in noun or slang in phr:
                return True
        # travelsaryEndTime = time.time()
        # print(f"All of Dataset Travelsary : {travelsaryEndTime - travelsaryStartTime:.5f}sec")
        return False


if __name__ == "__main__":
    koslang = koslang()
    exp = input("Input test sentence : ")
    print(koslang.isSlang(exp))


