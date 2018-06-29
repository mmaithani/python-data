import re    #importing regular expression module
# #1.
# print("hello \n world")        #here when / is come in between hello world then interpreter takes next alphabet to / as a special character
# print(r"hello \n world")       #now output is print as it is as a raw data
#
# # 2.
# print("search")
# s="This is a test string"
# p=re.compile(r"t")            #find small-t from string (10,11)which means t is found at 10th location and stop at 11
# result=p.search(s)
# print(result)
#
# #3.
# print("match=================>")           #if we want to check that particular string start with same or not
# s="This is a test string"
# p=re.compile(r"t")                        #match will only check for first character
# result=p.match(s)
# print(result)
#
# #4.
# print("4.  findall=====================>")
# s="This is a test string"
# p=re.compile(r"s")                     #find all the search character from given string and print
# result=p.findall(s)
# print(result)
#
# #5.
# print("5. finditer=>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# s="This is a test string"

#
# #6.
# print("6. substring=>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# s="This is a test string"
# p=re.sub(r"s","b",s)            #replace s with r
# print(p)
#
# #7===============================================================================================================================.
s="this i.s a string. >sdc+ = =+" \
  "dnlkdnnd" \
  "zcnvlknklvnlkna"   "aaa aba aca ana aab aaaa aaab" \
  "v klsn dvnsv46f84856" \
  " " \
  "5T" \
  "5(0.." \
  "65 " \
  "6"
# p=re.compile(r"^t")            #find #\s  \d \S   "^t"=there is t at satrt of string        \b=word boundry             \B. .
# result=p.finditer(s)
# for r in result:
#     print(r)
#
#
# p=re.compile(r"a[abc]a")      #frim 45 kine      #find which have start a ending a and middle can be either a or b or c                                  #\s  \d \S   "^t"=there is t at satrt of string        \b=word boundry             \B. .
# result=p.finditer(s)
# for r in result:
#     print(r)
#
#       find which have start a ending a and middle can be either a or b or c
#
#
# p = re.compile(r"a[a-z]a")  #setting range find word having a on starting and ending and anything iun middle
# result=p.finditer(s)
# for r in result:
#     print(r)
#
# p=re.compile(r"a[A-Za-z]a")      #settting multiple range
# for r in result:
#     print(r)
#
# p=re.compile(r"a[A-Za-z][a-z]")      #find who have a in starting and atoz in middle and a to z in last
# result=p.finditer(s)
# for r in result:
#     print(r)
#
# p=re.compile(r"a+")      #quantifiers=here we find string at least one a at starting
# result=p.finditer(s)
# for r in result:
#     print(r)
#
# p=re.compile("a*")      #if zero 'a' match or more
# result=p.finditer(s)
# for r in result:
#     print(r)
#
# p=re.compile(r"aab?")      #find 'b' at last prsent or not
# result=p.finditer(s)
# for r in result:
#     print(r)
#
# p=re.compile("a{2,3}")      #find a which come at least 2 and maximum 3
# result=p.finditer(s)
# for r in result:
#     print(r)
#
# p=re.compile(r"[^ab]")      #   '^' inside the bracket meanns inversion
# result=p.finditer(s)
# for r in result:
#     print(r)
#
# p=re.compile(r"a[abc]a a[abc]a")      #find patttern like'aaa aba' or 'aba aca'
# result=p.finditer(s)
# for r in result:
#     print(r)
#
#p=re.compile("(a[abc]a) (a[abc]a)")      #
# result=p.finditer(s)
# for r in result:
#     print(r)
#
#..........................................................................................................................................
#
# s="This is test string"
# p=re.compile(r"(.*) is (.*) (.*)")
# result=p.match(s)
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))



