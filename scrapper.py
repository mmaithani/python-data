import re
import requests
import datetime
import xlsxwriter
import urllib.request
from bs4 import BeautifulSoup
from collections import OrderedDict
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize

# url = "https://api.slack.com/faq"
# url = "https://amazon.jobs/en-gb/faqs"
url = "https://help.twitter.com/en/using-twitter/following-faqs"
# url = "https://www.godrejproperties.com/nricorner/nri-faqs"
# url = "https://www.ibm.com/support/customer/in/en/contractsfaq.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
all_stopwords = stopwords.words('english')
stop = ['\'s',',','``','\"\"','\'\'','.','!','how','How','Can','can','what','What','where','Where','describe','Describe','Who','who','When','Whom','whom','when','Why','why','Should','should','is','Is','I','Do','do','Are','are','Will','will','If','if','In','in','Explain','explain','?']
for sd in stop:
    all_stopwords.append(sd)



################################################################################################################### 
#                                         Find QUES_TAG & QUES_CLASS if exists
################################################################################################################### 



questions = []
for elem in soup(text=re.compile(r'\s*((?:how|How|Can|can|what|What|where|Where|describe|Describe|Who|who|When|Whom|whom|when|Why|why|Should|should|is|Is|I|Do|do|Are|are|Will|will|If|if|In|in|Explain|explain)[^.<>?]*?\s*\?)')):
    # print(elem.parent)
    questions.append(elem.parent)
# print(len(questions))
x = str(questions[2])
ques_tag = x[x.find("<") + 1 : x.find(">")]
if "class" in ques_tag:
    class_name_ques = ques_tag.split("class=\"")[1].replace("\"", "")
    print("class :",class_name_ques)
else:
    class_name_ques = None
ques_tag = str(ques_tag).split(" ")[0]
if ques_tag == "script":
    x = str(questions[4])
    ques_tag = x[x.find("<") + 1 : x.find(">")]
    ques_tag = str(ques_tag).split(" ")[0]
print('ques_tag :', ques_tag)
if class_name_ques is not None:
    questions_unfiltered  = soup.find_all(ques_tag, {"class" : class_name_ques})
else:
    questions_unfiltered  = soup.find_all(ques_tag)
# print(questions_unfiltered, len(questions_unfiltered))



################################################################################################################### 
#                                         Extract Questions
################################################################################################################### 


questions = []
for ques in questions_unfiltered:
    questions.append(str(ques.text).replace("\n","").replace("\t","").replace("  ",""))
questions = [q for q in questions if q.endswith("?")]
print(questions, "\n", len(questions))



################################################################################################################### 
#                                         Remove Stopwords
################################################################################################################### 



questions_without_sw = []
for q in questions:
    text_tokens = word_tokenize(q)
    tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
    questions_without_sw.append(" ".join(tokens_without_sw))
    # questions_without_sw.append(tokens_without_sw)
print(questions_without_sw, "\n", len(questions_without_sw))



################################################################################################################### 
#                                         Extract Answers
###################################################################################################################  



answers = []
# for qs in questions_without_sw:
#     for da in soup.find_all(['div','p','li','a']):
#         if (da.text).find(qs) and len(da.text) > 20:
#             print(da.text.replace("\n", "").replace("  ",""))
#             break
#     break
for k in questions_unfiltered:
    # print(k)    
    for l in k.next_siblings:
        # print(l.name)
        if (l.name == 'p' or l.name == 'li' or l.name == 'a' or l.name == "div"): 
            answers.append(str(l.text).replace("\n","").replace("\t",""))
        elif l.name == ques_tag:
            continue
    if len(answers) == len(questions):
        break

answers = list(dict.fromkeys(answers))[:len(questions)]
print(answers, "\n" ,len(answers))



################################################################################################################### 
#                                         Extract Answers
################################################################################################################### 



# answers = []
# for k in questions_unfiltered:
#     # print(k)    
#     for l in k.next_siblings:
#         # print(l, l.name)
#         if (l.name == 'p' or l.name == 'li' or l.name == 'a' or l.name == "div"): 
#             answers.append(str(l.text).replace("\n","").replace("\t",""))
#         elif l.name == ques_tag:
#             continue
#     if len(answers) == len(questions):
#         break

# answers = list(dict.fromkeys(answers))[:len(questions)]
# print(answers, "\n" ,len(answers))



###################################################################################################################


# pageContent=requests.get('https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo')
# pageContent=requests.get("https://help.twitter.com/en/using-twitter/following-faqs")
# tree = html.fromstring(pageContent.content)
# for j in range(1,3):
#     for i in range(1,4):
#         goldWinners=tree.xpath('/html/body/main/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[{}]/div/div/div/div[2]/ul/li[{}]/text()'.format(j,i))
#         print(goldWinners)


# for t in tree:
#   print(t)
# goldWinners=tree.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td[2]/a[1]/text()')
# silverWinners=tree.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td[3]/a[1]/text()')
# bronzeWinners=tree.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td[4]/a[1]/text()')
# medalWinners=goldWinners+silverWinners+bronzeWinners
# print(goldWinners, silverWinners, bronzeWinners, medalWinners)
# for name in medalWinners:
#     print(name)