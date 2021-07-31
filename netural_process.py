from konlpy.tag import Okt as kk 
import sys

from konlpy.utils import select

kkma = kk()
senlist = []
sdic = {}

def process(sen) -> list: 
    s = kkma.pos(sen)
    for i in s :
        if i[1] == 'Noun' or i[1] == 'Verb' or i[1] == 'Adjective':
            senlist.append(i[0])
    print(senlist)
        # senlist = []


def Noun(sen) -> list :
    s = kkma.pos(sen)
    for i in s :
        if i[1] == 'Noun' :
            senlist.append(i[0])
    print(senlist)
        # senlist = []


def Verb(sen) -> list :
    s = kkma.pos(sen)
    for i in s :
        if i[1] == 'Verb' :
            senlist.append(i[0])
    print(senlist)
        # senlist = []


def Adjective(sen) -> list :
    s = kkma.pos(sen)
    for i in s :
        if i[1] == 'Adjective' :
            senlist.append(i[0])
    print(senlist)
        # senlist = []



if __name__ == '__main__' :
    if sys.argv[1] == 'noun' :
        Noun(sys.argv[2])
    if sys.argv[1] == 'verb' :
        Verb(sys.argv[2])
    if sys.argv[1] == 'adjective' :
        Adjective(sys.argv[2])
    if sys.argv[1] == None :
        process(sys.argv[2])
