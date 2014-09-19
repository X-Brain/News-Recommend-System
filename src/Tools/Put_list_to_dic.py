import Find_Top
def   list_to_dic():
     fr = open('/Users/hakuri/Desktop/train_date_set1.txt')
     fr1=open('/Users/hakuri/Desktop/train_lastday_set1.txt')
     f=open('/Users/hakuri/Desktop/lastday_fit_hot_5.txt','w')
     dic={}
     for i in range(1,32):
        list=[]
        dic[i]=list
     for line in fr.readlines():
        dic[int(line.strip().split('\t')[4])].append(line.strip().split('\t')[1])   
     print dic
     
     for k, v in dic.iteritems():
        dic[k]=  Find_Top.find_top(v, 5)
     print dic
     for line1 in fr1.readlines():
        for i in range(0,5):
           print  line1.strip().split('\t')[0]+'\t'+dic[int(line1.strip().split('\t')[4])][i]+'\n'
           f.write(line1.strip().split('\t')[0]+'\t'+dic[int(line1.strip().split('\t')[4])][i]+'\n') 
#        f.write(k+'\t')
#        for m in v:
#              f.write(m+',')
#        f.write('\n')    
list_to_dic()