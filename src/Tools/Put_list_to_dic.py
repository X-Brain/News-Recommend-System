def   list_to_dic():
     fr = open('/Users/hakuri/Desktop/train_date_set.txt')
     
     f=open('/Users/hakuri/Desktop/everyday_news.txt','w')
     dat=[]
     dat1=[]
     dic={}
     for i in fr.readlines():
         dat.append(i)
     dat1=dat
        
     for line in dat:       
        list=[]
        for line1 in dat1:
             
            if line.strip().split('\t')[4]==line1.strip().split('\t')[4]:
                
                list.append(line1.strip().split('\t')[1])
           
        dic[line.strip().split('\t')[4]]=list
     for k, v in dic.iteritems():
       f.write(k+'\t')
       for m in v:
             f.write(m+',')
       f.write('\n')    
list_to_dic()