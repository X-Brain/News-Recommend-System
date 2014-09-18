def find_top(list,number):
    top_list=[]
    for j in range(0,number):
       items = dict([(list.count(i), i) for i in list])
       max_value=items[max(items.keys())]
       top_list.append(max_value)
       list=delect_key(list,max_value)
    return top_list
    
       
def delect_key(list,key):
    for i in list:
        if i==key:
            list.remove(key)
    return list        

if __name__=='__main__':
    list=['33','1','412','1','35','33','412','412']
    print find_top(list,3)