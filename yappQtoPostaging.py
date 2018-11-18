from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

f = open('yappQ.txt',mode='r',encoding='utf-8')
question = f.read()
f.close()
s = open('yappQPostag.txt',mode='w',encoding='utf-8')
qlist = kkma.pos(question)
for i in qlist:
	s.write(''.join("{}\t{}".format(i[0],i[1]))+"\n")
s.close()