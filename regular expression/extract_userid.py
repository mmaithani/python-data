# Q.1- Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com" "page33@google.com"
# "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

#ANs.1
import re
mail="zuck26@facebook.com" \
       "page33@google.com" \
       "jeff42@amazon.com"
# domain=re.findall(r"\w+@.*",mail)
# domain=re.findall(r"\w+@\w+\.(?:com|in)",mail)
# domain=re.search('@*?\.',mail)
# userid = re.search(".[\w.]+", mail)
# domain = re.search("@[\w.]+", mail)
# print(userid.group())
# print(domain.group())
# company=re.compile(r".")
# result1=company.search(mail)
# print(result1.group())
# suffix=re.compile(r"..m")
# result=suffix.search(mail)
# print(result.group())

p= re.compile("([A-Za-z0-9._]+)@([A-Za-z0-9]+)\.([A-Za-z]+)")
result=p.match(mail)
print(result.group(1))
print(result.group(2))
print(result.group(3))
