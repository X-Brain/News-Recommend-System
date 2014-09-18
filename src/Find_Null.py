def Find_Null():
    fr = open('/Users/hakuri/Desktop/train_set.txt')
    fr1 = open('/Users/hakuri/Desktop/first_upload.txt')
    f=open('/Users/hakuri/Desktop/null_v.txt','w')
    f1=open('/Users/hakuri/Desktop/null_k.txt','w')
    list=[]
    dic={}
    v_list=[]
    k_list=[]
    for line in fr.readlines():
#         if cmp(line.strip().split('\t')[4],'null')==-1:
       
        
        if line.strip().split('\t')[4]=='NULL' and line.strip().split('\t')[3]!='404':
                 list.append(line.strip().split('\t')[1])
               
    for i in list:
        n=1
        for j in list:
            if i==j:
                n=n+1
            else :
                n=n 
        dic[i]=n        
        list.remove(i)
    
    for k, v in dic.iteritems():
        if v>30:
            v_list.append(k)
            
#             f.write(k+'\n')
          
#     print list      
#     print dic      
    for line in fr1.readlines():
                if line.strip().split('\t')[1] in list:
                    k_list.append(line.strip().split('\t')[0])
    for x in k_list:
        for y in v_list:
            f1.write(x+'\t'+y+'\n')                
Find_Null()