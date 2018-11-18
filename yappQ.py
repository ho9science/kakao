from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

f = open('yappArrange.txt',mode='r',encoding='utf-8')
question = f.read()
pprint(kkma.pos(question))