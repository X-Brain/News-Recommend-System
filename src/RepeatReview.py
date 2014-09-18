'''
@author: Garvin
'''
import csv

def Find_LastReview():

     fr = open('/Users/hakuri/Desktop/train_date_set.txt')
     f=open('/Users/hakuri/Desktop/test.txt','w')
     dic={}

     for line in fr.readlines():
        # line.strip().split('\t')
         dic[line.strip().split('\t')[0]]=line.strip().split('\t')[1]+'\t'+line.strip().split('\t')[2]+'\t'+line.strip().split('\t')[3]+'\t'+line.strip().split('\t')[4]
         
     for key in dic:
         print key,dic[key] 
         f.write(key+'\t'+dic[key]+'\n')  
if __name__=='__main__':
    Find_LastReview()