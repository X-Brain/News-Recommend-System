import WordSplite_test.Global_param

distance_time=10000

def Get_last():
     f1=open(WordSplite_test.Global_param.test_root+'test/train_date_set1.txt')
     f2=open(WordSplite_test.Global_param.test_root+'test/train_date_set1.txt')
     f3=open(WordSplite_test.Global_param.test_root+'test/train_date_set1.txt')
     fr=open(WordSplite_test.Global_param.test_root+'test/train_lastdat_constant_set1.txt','w')
     dic={}
     for line in f1.readlines():
         list2=[]
         dic[line.strip().split('\t')[0]]=list2
     for line1 in f2.readlines():
         dic[line1.strip().split('\t')[0]].append(int(line1.strip().split('\t')[2]))    
     
     for k,v in dic.iteritems():
         list1=list(set(v))
         print list1
         t1=max(list1)
         print t1
         list1.remove(t1)
         print list1
         if list1:
           t2=max(list1)
           print t2
           print t1-t2
         else :
           t2=-5000
         if (t1-t2)<=distance_time:
           dic[k]=str(t1)
     
     for line2 in f3.readlines():
         if dic[line2.strip().split('\t')[0]]==line2.strip().split('\t')[2]:
             fr.write(line2)
Get_last()             
             

             