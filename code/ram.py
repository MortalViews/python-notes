
1.

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
 [[row[i] for row in matrix] for i in range(4)]

O/p:
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

2.

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

3.

>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
>>> string1, string2, string3 = '', 'T', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'T'
>>> string1, string2, string3 = 'u', 'T', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'u'
>>> string1, string2, string3 = 'a', 'T', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'a'
>>> string1, string2, string3 = 'a', 'T', 'Hammer Dance'
>>> non_null = string1 and string2 or string3
>>> non_null
'T'
>>> string1, string2, string3 = '', 'T', 'Hammer Dance'
>>> non_null = string1 and string2 or string3
>>> non_null
'Hammer Dance'
>>> non_null = string1 and string2 and string3
>>> non_null
''
>>> string1, string2, string3 = '', 'T', 'Hammer Dance'
>>> non_null = string1 and string2 and string3
>>> non_null
''