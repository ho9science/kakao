from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

f = open('yappArrange.txt',mode='r',encoding='utf-8')
question = f.read()
f.close()
s = open('yappQArrange.txt',mode='w',encoding='utf-8')
qlist = kkma.nouns(question)
for i in qlist:
	s.write(i+"\n")
s.close()