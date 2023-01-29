from datetime import datetime
from collections import Counter
import sys
sites={}
dat = sys.argv[1]
with open("server.log") as f:
    for elem in f:
        s= elem.split()
        s_date=s[1][1:-10]
        g=datetime.strptime(s_date, '%d/%b/%Y').date().strftime('%d.%m.%Y')
        if g !=dat:
          continue
        key= g+s[3]
        if key in sites:
            sites[key]+=1
        else:
           sites.setdefault(key, 1) 
bow_3 = Counter(sites)
result = bow_3.most_common(1)
print(result[0][0][10:],result[0][1])

        
