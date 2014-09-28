import Global_param
#coding=utf-8  
def TransforData(day):
    
     fr = open(Global_param.test_root+'test/train_lastdat_constant_set1.txt')
     f=open(Global_param.test_root+'test/train_lastday_set/train_lastday_set1_%d.txt'%day,'w')
     for line in fr.readlines():
        # line.strip().split('\t')
         t= line.strip().split('\t')[4]
         if int(line.strip().split('\t')[4])==day:
               f.write(line)
        
def TransforDataset(day):
    
     fr = open(Global_param.test_root+'test/train_date_set1.txt')
     f=open(Global_param.test_root+'test/train_date_set1/train_date_set1_%d.txt'%day,'w')
     for line in fr.readlines():
        # line.strip().split('\t')
         t= line.strip().split('\t')[4]
         if int(line.strip().split('\t')[4])==day:
               f.write(line)        
        
# if __name__=='__main__':
#     TransforData()