#Q.3- Split the following irregular sentence into words
import re
sentence = "A,very very; irregular_sentence"
#desired_output = "A very very irregular sentence"
# p= re.compile("([A-Za-z0-9., :;_]+)")
# result=p.match(sentence)
# print(result.group(1))

# print(result.group(1))
p=re.sub("[^A-Za-z0-9]"," ",sentence)
print(p)