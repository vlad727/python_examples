import re

# some data
file = "aaaaa, 190000, 202020,  january, irina, google.com, mail.ru,\
        alex, intercom, cat, cats, dog, dogs, 2002, 2022, TV, calculator,\
        qqqqcvv, gggg, paper , vegetables , fruits, maks, spaace, mars, march, my_email@mail.com, your_email.com,\
        etc., yandex.ru, cat@yandex.ru, 123, 12, 1111, Vlad, Andrey"
"""
\d = any digit 0-9
\D = any non digit, any char
\w = any letter [A-Z] [a-z]
\W = any char beside letters [, . ? } | @ ]
\s = breakspace 
\S = non breakspace
[0-9][3] = 3 any digit  
[A-z][a-z]+ # word start with Upper letter then small letters
\w+\.\w+
"""
# what we try to find
#find = r"\d\d\d" # any 3 digit result: ['190', '000', '202', '020', '200', '202', '123', '111']
#find = r"[0-9]{4}" # result: ['1900', '2020', '2002', '2022', '1111']
#find = r"\w{6}" # result: ['190000', '202020', 'januar', 'google', 'interc', 'calcul', 'qqqqcv', 'vegeta', 'fruits', 'spaace', 'my_ema', 'your_e', 'yandex', 'yandex']
#find  = r"\w{6}\s" # result: ['tables ']
#find = r"yandex" # search only word yandex result:  ['yandex', 'yandex']
#find = r"[A-Z][a-z]+" # ['Vlad', 'Andrey']
#find = r"\w+\.\w+" # any word then . and any word # ['google.com', 'mail.ru', 'mail.com', 'your_email.com', 'yandex.ru', 'yandex.ru']
find = r"[A-Z][a-z]+" # ['@mail.com', '@yandex.ru']
# output result to var result
result = re.findall(find, file)
# find - what we try to find
# file - where we try to find
# output our result
print(result)
