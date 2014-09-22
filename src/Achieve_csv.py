import csv

def Achieve_csv():
    fr = open('/Users/hakuri/Desktop/result.txt')
    csvf=open('/Users/hakuri/Desktop/test.csv','wb')
    writer=csv.writer(csvf)
    writer.writerow(['userid','newsid'])
    for line in fr.readlines():
        writer.writerow([line.strip().split('\t')[0],line.strip().split('\t')[1]])
  
   
Achieve_csv()        