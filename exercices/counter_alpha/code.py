from collections import Counter
import string 

l =string.ascii_lowercase[::-1]
TIE='tie'
FIRST_WIN='first_win'
SECOND_WIN='second_win'

def match(s):
    ls = s.split()
    if not all(map(str.isalpha,ls)) or\
        any(map(lambda x: 'no' in x,ls)):
        return TIE

    sc1,sc2=map(Counter,ls)

    for c in l:
        if sc1[c] == sc2[c]:
            continue	
        return FIRST_WIN if sc1[c] > sc2[c] else SECOND_WIN
    return TIE

if __name__=="__main__":
   assert match('zaay zaac&') ==TIE
   assert match('adflkj# fawefkj')==TIE
   assert match('awefnoafwe fakwjefzzzz')==TIE
   assert match('awezzzfnyyzoafwe fazkwjzyefzz')==FIRST_WIN
   assert match('abcdefg hijklmn')==SECOND_WIN
