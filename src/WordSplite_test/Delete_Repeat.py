import Global_param
#coding=utf-8  
def Delete_Repeat():
 
     f=open(Global_param.test_root+'test/result.txt')
     f1=open(Global_param.test_root+'test/train_date_set1.txt')
     f2=open(Global_param.test_root+'test/train_date_set1.txt')
     fr=open(Global_param.test_root+'test/result_no_repeat.txt','w')
     dic={}
     num=0
     for line in f1.readlines():
         list=[]
         dic[line.strip().split('\t')[0]]=list     
    
     for line1 in f2.readlines():
          dic[line1.strip().split('\t')[0]].append(line1.strip().split('\t')[1])
     
     print "Delete_Repeat 消除重复项，推荐列表中去重已经阅览过的"
     
     for line2 in f.readlines():
        try:
          if line2.strip().split('\t')[1] not in dic[line2.strip().split('\t')[0]]:
              fr.write(line2)
              num=num+1
             
        except:
            continue
     print num

          
Delete_Repeat()         
    