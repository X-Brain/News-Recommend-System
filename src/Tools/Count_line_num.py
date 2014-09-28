import WordSplite_test.Global_param

#coding=utf-8  
def count_line():
   f=open('/Users/hakuri/Desktop/test/result_no_repeat_hot.txt')
   f1=open('/Users/hakuri/Desktop/test/train_lastdat_constant_set1.txt')
   i=0
   i1=0
   for line in f.readlines():
       i=i+1
   print 'the number of commits %d'%(i)    
   for line1 in f1.readlines():
       i1=i1+1
   print 'number of predict users %d'%(i1)

count_line()