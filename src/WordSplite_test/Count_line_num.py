
def count_line():
   f=open('/Users/hakuri/Desktop/test/result_no_repeat.txt')
   i=0
   for line in f.readlines():
       i=i+1
   print i    

count_line()