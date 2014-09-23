import csv
import codecs
def Achieve_csv():
    fr = open('/Users/hakuri/Desktop/result.txt',codecs.BOM_UTF8)
    csvf=open('/Users/hakuri/Desktop/test.csv','wb')
    writer=csv.writer(csvf)
    i=0
    writer.writerow(['userid','newsid'])
    
    for line in fr.readlines():
        
        a=int(line.strip().split('\t')[0])
        b=int(line.strip().split('\t')[1])
        if i<=50000:
         writer.writerow([a,b])
         i=i+1
        else:
            break
Achieve_csv()        