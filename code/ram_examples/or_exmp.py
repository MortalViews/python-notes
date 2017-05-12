string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3

print(non_null)


# non_null
# 'Trondheim'
string1, string2, string3 = '', 'T', 'Hammer Dance'
non_null = string1 or string2 or string3

# non_null
# 'T'
string1, string2, string3 = 'u', 'T', 'Hammer Dance'
non_null = string1 or string2 or string3
# non_null
# 'u'
string1, string2, string3 = 'a', 'T', 'Hammer Dance'
non_null = string1 or string2 or string3

# non_null
# 'a'
string1, string2, string3 = 'a', 'T', 'Hammer Dance'
non_null = string1 and string2 or string3

string1, string2, string3 = 'a', 'T', 'Hammer Dance'
non_null = (string1 and string2) or string3