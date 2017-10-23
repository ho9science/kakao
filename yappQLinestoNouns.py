from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

f = open('yappArrange.txt',mode='r',encoding='utf-8')
s = open('yappQArrange.txt',mode='w',encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
	qlist = kkma.nouns(line)	
	for i in qlist:
		s.write(i)
	s.write("\n")

s.close()