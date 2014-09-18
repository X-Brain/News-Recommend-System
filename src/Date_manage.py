def Date_Manage():
     fr = open('/Users/hakuri/Desktop/train_set.txt')
     f=open('/Users/hakuri/Desktop/train_date_set.txt','w')
     for line in fr.readlines():
          if '2014' in line.strip().split('\t')[4] and '03' in line.strip().split('\t')[4]:
           print line.strip().split('\t')[4][12:14]
           f.write(line.strip().split('\t')[0]+'\t'+line.strip().split('\t')[1]+'\t'+line.strip().split('\t')[2]+'\t'+line.strip().split('\t')[3]+'\t'+line.strip().split('\t')[4][12:14]+'\n')


Date_Manage()
