'''
@author: Garvin
'''
def TransforData():
    
     fr = open('/Users/hakuri/Desktop/data_set.txt')
     f=open('/Users/hakuri/Desktop/train_set.txt','w')
     for line in fr.readlines():
        # line.strip().split('\t')
         tab='\t'
         line_change=line.strip().split('\t')[0]+tab+line.strip().split('\t')[1]+tab+line.strip().split('\t')[2]+tab+line.strip().split('\t')[3]+tab+line.strip().split('\t')[5]
         print line_change
         f.write(line_change+'\n')
         
if __name__=='__main__':
    TransforData()