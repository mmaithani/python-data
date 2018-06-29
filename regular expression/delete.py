# Q.1- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# desired_output = 'Good advice What I would do differently if I was learning to code today'
p=re.sub("[^A-Za-z0-9]", " ", tweet)
print(p)
