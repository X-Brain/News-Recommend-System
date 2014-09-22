def Get_keynews(day):
    fr = open('/Users/hakuri/Desktop/test/key_words/keywords_%d.txt'%day)
    fr1 = open('/Users/hakuri/Desktop/test/train_date_set1/train_date_set1_%d.txt'%day)
    fr2=open('/Users/hakuri/Desktop/test/train_lastday_set/train_lastday_set1_%d.txt'%day)
    f=open('/Users/hakuri/Desktop/test/result.txt','a')
    list_key=[]
    dic={}
    dic_no_repeat={}
    for line in fr.readlines():
        print line
        for i in range(0,5) :
          list_key.append(line.strip().split('\t')[i])
   
    for m in list_key:     
        dic[m]=[]
    
    for line in fr1.readlines():
        for j in list_key:
            if j in line.strip().split('\t')[3]:
                dic[j].append(line.strip().split('\t')[1])
    for k,v in dic.iteritems():
         dic[k]=list(set(v))
                    
    print dic
    for line in fr2.readlines():
        list1=[]
        dic_no_repeat[line.strip().split('\t')[0]]=list1
        for k,v in dic.iteritems():
            if k in line.strip().split('\t')[3]:                
                for i in v:
                    dic_no_repeat[line.strip().split('\t')[0]].append(i)
        dic_no_repeat[line.strip().split('\t')[0]]= list(set(dic_no_repeat[line.strip().split('\t')[0]]))       
#                     print line.strip().split('\t')[0]+'\t'+i
    print     dic_no_repeat     
    for k1,v1 in  dic_no_repeat.iteritems():
        if v1:
            for m in v1:
              f.write(k1+'\t'+m+'\n')    

# Get_keynews()