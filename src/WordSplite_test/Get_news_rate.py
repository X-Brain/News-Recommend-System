import Global_param
#coding=utf-8  
def get_news_rate():
     fr = open(Global_param.train_set)
     fr1=open(Global_param.train_set)
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
#      print news_dic
     print "Get_news_rate 计算新闻出现的热度"
     return news_dic
     
get_news_rate()