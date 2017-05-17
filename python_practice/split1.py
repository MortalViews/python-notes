#!/usr/bin/python
str1 = "Line1-abcdef \nLin\ne2-abc \nLine4-abcd"
print (str1.split())
print (str1.split(" ",1))
print (str1.splitlines( num=string.count('\n')))


