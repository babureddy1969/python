s='''For the past 20 years, Melinda Gates has worked on the foundation she started with her husband, Microsoft co-founder Bill Gates, traveling the world on a mission to tackle poverty, hunger, health crises and other economic and education challenges.'''
'''
the 4
past 1
Melinda 1
Gates 2
'''
'''
word = {'milinda':3, 'past':2}
'''
words = s.replace(',','').replace('.','').split()
# uniqueWords = set(words)
wordcount={}
for word in words:
    wordcount[word] = wordcount.get(word,0) + 1
print(wordcount)

# s='madam'
# # s == ''.join([s[i] for i in range(len(s),-1,-1)])

# s = 'ABC'
# for a in s:
#     for b in s[1]:
#         for c in s:
#             print (a,b,c)