def   list_to_dic():
     fr = open('/Users/hakuri/Desktop/train_date_set1.txt')
     
     f=open('/Users/hakuri/Desktop/everyday_news.txt','w')
     dic={}
     for i in range(1,32):
        list=[]
        dic[i]=list
     for line in fr.readlines():
        dic[int(line.strip().split('\t')[4])].append(line.strip().split('\t')[1])   
     print dic
#      for k, v in dic.iteritems():
#        f.write(k+'\t')
#        for m in v:
#              f.write(m+',')
#        f.write('\n')    
list_to_dic()