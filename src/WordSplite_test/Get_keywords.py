import jieba.analyse
#!coding=utf-8
def Get_keywords(day):
    fr = open('/Users/hakuri/Desktop/test/train_date_set1/train_date_set1_%d.txt'%day)
    f1=open('/Users/hakuri/Desktop/test/key_words/keywords_%d.txt'%day,'w')
    txt=''
    for line in fr.readlines():
          txt=txt+line.strip().split('\t')[3]+','
    t= jieba.analyse.extract_tags(txt,5)   
    for i in t:
       f1.write(i+'\t')
    
# Get_keywords()     