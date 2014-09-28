import WordSplite_test.Global_param
f1=open(WordSplite_test.Global_param.test_root+'test/train_date_set1.txt')
f2=open(WordSplite_test.Global_param.test_root+'test/train_date_set1.txt')
f3=open(WordSplite_test.Global_param.test_root+'test/train_date_set1.txt')
fr=open(WordSplite_test.Global_param.test_root+'test/train_lastdat_set1.txt','w')
def Get_last():
    
    
     dic={}
     for line in f1.readlines():
         list=[]
         dic[line.strip().split('\t')[0]]=list
     for line1 in f2.readlines():
         dic[line1.strip().split('\t')[0]].append(int(line1.strip().split('\t')[2]))    
     
     for k,v in dic.iteritems():
         dic[k]=str(max(v))
     
     for line2 in f3.readlines():
         if dic[line2.strip().split('\t')[0]]==line2.strip().split('\t')[2]:
             fr.write(line2)
         

Get_last()


   