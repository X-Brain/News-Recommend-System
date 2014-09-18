'''
@author: Garvin
'''
def TransforData():
    
     fr = open('/Users/hakuri/Desktop/train_date_set.txt')
     f=open('/Users/hakuri/Desktop/train_date_set1.txt','w')
     for line in fr.readlines():
        # line.strip().split('\t')
         t= line.strip().split('\t')[4]
         if line.strip().split('\t')[4][0]=='0':
               t=line.strip().split('\t')[4][1]
              
         f.write( line.strip().split('\t')[0]+'\t' +line.strip().split('\t')[1]+'\t' + line.strip().split('\t')[2] +'\t' +line.strip().split('\t')[3] +'\t' +t+'\n')     
        
        
if __name__=='__main__':
    TransforData()