# ML PART >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import numpy as np

data=pd.read_csv('sample.tsv',delimiter='\t',quoting=3,error_bad_lines=False)
datas=pd.read_csv('de.tsv',delimiter='\t',quoting=3)


n = data.size/2
n1 = datas.size/2

print(n,n1)

corpus=[]
for i in range(0,n):
     rev=re.sub('[^a-zA-Z]',' ',data['Hai'][i])
     rev=rev.lower();
     rev=rev.split()
     ps=PorterStemmer()
     rev=[ps.stem(word) for word in rev if not word in set(stopwords.words('english'))]
     rev=' '.join(rev)
     corpus.append(rev)

corpus1=[]
for i in range(0,n1):
     rev=re.sub('[^a-zA-Z]',' ',datas['yes'][i])
     rev=rev.lower();
     rev=rev.split()
     ps=PorterStemmer()
     rev=[ps.stem(word) for word in rev if not word in set(stopwords.words('english'))]
     rev=' '.join(rev)
     corpus1.append(rev)    

     

for j in range(n1) :
    corpus.append(corpus1[j])     



X=pd.DataFrame(X)

X_test = X.tail(n1)

      
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()
Y=data.iloc[:,1].values    



X=X.iloc[0:n,:].values

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X,Y)

y_predict = classifier.predict(X_test)


y_predict=pd.DataFrame(y_predict)

arr = []

for index, row in y_predict.iterrows():
    print(row[0])
    arr.append(row[0])


print(arr)


cnt=0
snt=0
pnt=0
tnt=0

for j in arr :
    if j==1 :
        cnt+=1
    elif j==2:
        snt+=1
    elif j==3:
        tnt+=1
    elif j==4:
        pnt+=1
        
print(cnt,snt,tnt,pnt)

import matplotlib.pyplot as plt
slices_hours = [cnt, snt,tnt,pnt]
activities = ['MACHINE_LEARNING', 'ANDRIOD_APPLICATION','WEB_DEVELOPMENT','SOFTWARE_ENGINEERING']
colors = ['r', 'g','blue','cyan']
plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()
