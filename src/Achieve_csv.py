import csv
def Achieve_csv():
    fr = open('/Users/hakuri/Desktop/null_k.txt')
    csvf=open('/Users/hakuri/Desktop/null_v.csv','wb')
    writer=csv.writer(csvf)
    for line in fr.readlines():
        writer.writerow([line.strip().split('\t')[0],line.strip().split('\t')[1]])

  
Achieve_csv()        