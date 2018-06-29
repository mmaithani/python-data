# Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
import re
ret=[]
text = "Betty bought a bit of butter, But the butter was so bitter," \
       " So she bought some better butter, To make the bitter butter better."

p=re.compile(r"[bB][a-zA-Z]+")      #frim 45 kine      #find which have start a ending a and middle can be either a or b or c                                  #\s  \d \S   "^t"=there is t at satrt of string        \b=word boundry             \B. .
result=p.finditer(text)
for r in result:
    print(r)