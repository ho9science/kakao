from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

f = open('yappQ.txt',mode='r',encoding='utf-8')
question = f.read()
f.close()
s = open('yappQSentence.txt',mode='w',encoding='utf-8')
qlist = kkma.sentences(question)
for i in qlist:
	s.write(i+"\n")
s.close()