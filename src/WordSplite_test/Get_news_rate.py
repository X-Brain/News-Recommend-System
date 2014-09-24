def get_news_rate():
     fr = open('/Users/hakuri/Desktop/test/train_date_set1.txt')
     fr1=open('/Users/hakuri/Desktop/test/train_date_set1.txt')
     news_list=[]
     news_dic={}
     for line in fr.readlines():
         news_list.append(line.strip().split('\t')[1])
         
     news_list=list(set(news_list))   
     
     for i in news_list:
         news_dic[i]=0
     
#      print news_list
     for line in fr1.readlines():
         news_dic[line.strip().split('\t')[1]]+=1
     print news_dic
     return news_dic
     
get_news_rate()