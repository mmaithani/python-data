import re
import requests
import datetime
import xlsxwriter
import urllib.request
from bs4 import SoupStrainer
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# url = "https://api.slack.com/faq"
# url = "https://www.netflix.com/in/"
# url = "https://amazon.jobs/en-gb/faqs"                                                                                                  
# url = "https://www.wired.com/about/faq/"  
url= "https://telegram.org/faq"                                            
# url = "https://www.godrejproperties.com/nricorner/nri-faqs"
# url = "https://www.ibm.com/support/customer/in/en/contractsfaq.html"
# url = "https://support.skype.com/en/faq/FA34713/faq-and-known-issues-with-skype"      # Questions' format?  
# url = "https://policies.google.com/faq?hl=en-US"
# url = "https://helpx.adobe.com/creative-cloud/faq.html#Basics"
# url = "https://www.newyorker.com/about/faq"                                           
# url = "https://www.time.com.my/support/faq"
# url = "https://techcrunch.com/2007/01/10/apple-iphone-faq/"
# url = "https://techcrunch.com/2009/06/09/frequently-asked-dtv-questions/"


################################################################################################################### 
#                                         Get all  Links from the website
################################################################################################################### 

parsed = urlparse(url)
hostname = parsed.hostname
hostname_old = hostname
try:
    pos_end = hostname.index('.', hostname.index('.') + 1)
    pos_start = hostname.index('.')
    hostname = hostname[pos_start +1 :]
except:
    pass
print(hostname_old, "-->", hostname)

def sitemap(url):
    links = []
    texts = []
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    all_links = soup.findAll('a')
    for link in all_links:
        try:
            if str(link).split("href=\"")[1].startswith("http") and hostname in str(link).split("href=\"")[1]:
                # print(str(link).split("href=\"")[1].split("\"")[0])
                links.append(str(link).split("href=\"")[1].split("\"")[0])
                texts.append(link.text.split("\n")[0])
        except:
            continue
    return links

all_links = sitemap(url)
# try:
#     sitemap1 = [s for s in all_links if 'sitemap' in s]
#     print(sitemap1)
#     if len(sitemap1) != 0:
#         t = sitemap(sitemap1[0])
#         print(t)
# except:
#     print(all_links)

################################################################################################################### 
#                                           Get FAQs
################################################################################################################### 

html = urllib.request.urlopen(url).read()
ques_initials = ['how','How','Can','can','what','What','where','Where','describe','Describe','Who','who','When','Whom','whom','when','Why','why','Should','should','is','Is','I','Do','do','Are','are','Will','will','If','if','In','in','Explain','explain']
soup_body = BeautifulSoup(html, "html.parser", parse_only = SoupStrainer("body"))
data = soup_body.get_text("\n", strip = True)
data = data.split("\n")
data_str = "".join(data)
# try:
#     print(data_str)
# except:
#     print(data_str.encode())

questions = soup_body.find_all(text=re.compile(r'\s*((?:how|How|Can|can|what|What|where|Where|describe|Describe|Who|who|When|Whom|whom|when|Why|why|Should|should|is|Is|I|Do|do|Are|are|Will|will|If|if|In|in|Explain|explain)[^.<>?]*?\s*\?)'))
questions = [q for q in questions if q.endswith("?") or q.endswith("? ") and q.split(" ")[0] in ques_initials and len(q.split(" ")) > 4]
questions = [q[0].replace(" ","") if q[0] == " " else q for q in questions]
questions = list(dict.fromkeys(questions))
# print(questions)
ques_index = []
for i in range(len(data)):
    if data[i] in questions:
        ques_index.append(data_str.find(data[i]))
# print(ques_index)

f = 0
ques = []
ans = []
while (f != len(ques_index)-1):
    if data_str[ques_index[f]:ques_index[f+1]] != "" and data_str[ques_index[f]:ques_index[f+1]].count("?") == 1:
        # print(f, "-->\n", data_str[ques_index[f]:ques_index[f+1]])
        ques.append(data_str[ques_index[f]:ques_index[f+1]].split('?')[0]+'?')
        ans.append(data_str[ques_index[f]:ques_index[f+1]].split('?')[1])
    # if data_str[ques_index[f]:ques_index[f+1]] != "" and data_str[ques_index[f]:ques_index[f+1]].count("?") > 1:
    #     # print(data_str[ques_index[f]:ques_index[f+1]])
    #     index =  [i for i, letter in enumerate(data_str[ques_index[f]:ques_index[f+1]]) if letter == '?']
    #     print(index)
    #     print(data_str[index[0]:index[1]+1])

    f += 1
for q,a in zip(ques, ans):
    try:
        print(q, a)
    except:
        print(q.encode(), a.encode())


################################################################################################################### 
#                                         Export to Excel
###################################################################################################################

# workbook = xlsxwriter.Workbook('web_{}.xlsx'.format(str(datetime.datetime.now())[:20]).replace(":","_"))
# worksheet = workbook.add_worksheet()
# bold = workbook.add_format({'bold': 1})
# worksheet.write('A1', 'Question', bold)
# worksheet.write('B1', 'Answer', bold)
# worksheet.set_column(1, 0, 100)
# worksheet.set_column(1, 1, 100)
# row = 1
# col = 0

# for q, a in zip(ques, ans):
#     worksheet.write_string(row, col, q)
#     worksheet.write_string(row, col + 1, a)
#     row += 1
# workbook.close()