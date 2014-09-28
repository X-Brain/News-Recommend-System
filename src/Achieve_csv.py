import csv
import WordSplite_test.Global_param
def Achieve_csv():
    fr = open(WordSplite_test.Global_param.test_root+'test/result_no_repeat_hot.txt')
    csvf=open(WordSplite_test.Global_param.test_root+'test/test.csv','wb')
    writer=csv.writer(csvf)
    i=0
    writer.writerow(['userid','newsid'])
    
    for line in fr.readlines():
       
       try :
        a=int(str(line.strip().split('\t')[0]))
        
        b=int(str(line.strip().split('\t')[1]))
    
        writer.writerow([a,b])
        i=i+1
         
        
            
            
       except:
            print line
            continue
        
Achieve_csv()        