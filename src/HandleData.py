'''
@author: Garvin
'''
def TransforData():
    
     fr = open('/Users/hakuri/Desktop/train_lastday_set1.txt')
     f=open('/Users/hakuri/Desktop/train_lastday_set1_5.txt','w')
     for line in fr.readlines():
        # line.strip().split('\t')
         t= line.strip().split('\t')[4]
         if int(line.strip().split('\t')[4])==5:
               f.write(line)
        
        
if __name__=='__main__':
    TransforData()