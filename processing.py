from konlpy.tag import Okt
okt = Okt()

text = '지금 뭐하고 있어?.'
text_dic = {}

text_nouns = okt.nouns(text)

for i in range(len(text_nouns)) :
    text_dic[text_nouns[i]] = True

if text_dic['뭐'] :
    print('지금은 탄생중')

print(text_dic)