from konlpy.tag import Okt

okt = Okt()
text = str(input())
text_dic = {}

text_nouns = okt.nouns(text)
    
for i in range(len(text_nouns)) :
    text_dic[text_nouns[i]] = True
print(text_dic)

try :
    if text_dic['뭐'] & text_dic['지금']:
        answer = '지금은 탄생중'
        print(answer)

except :
    print('뭐라고? 다시 말해줘')