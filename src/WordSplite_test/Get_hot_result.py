import Get_news_rate
import print_list_dic
import Global_param
#coding=utf-8  
def get_hot_result(top):
    f=open(Global_param.test_root+'test/result_no_repeat.txt')
    f1=open(Global_param.test_root+'test/result_no_repeat.txt')
    news_dic=Get_news_rate.get_news_rate()
    print news_dic
    user_list=[]
    dic={}
    for line in f.readlines():
        user_list.append(line.strip().split('\t')[0])
    user_list=list(set(user_list))
    for i in user_list:
        list1=[]
        dic[i]=list1
#     print dic
    for line in f1.readlines():
        dic[line.strip().split('\t')[0]].append(line.strip().split('\t')[1])
    
    for k,v in dic.iteritems():
      
        if len(v)>3:
            
            temp_list=[]         
            for j in v:
                 if news_dic[j]>top:
                    temp_list.append(j) 
#                 if news_dic[v[j]]>news_dic[temp_list[0]]:
#                      temp_list.remove(temp_list[0])
#                      temp_list.append(news_dic[v[j]])
            v= temp_list   
            
        dic[k]=v  
#coding=utf-8                   
    print 'Get_hot_result finished'
    print_list_dic.print_dic(dic)
# get_hot_result(1)