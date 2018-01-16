
##Created Date : 170-Jan-2018
##@ Author : Vishal R

import  operator, numpy as np, json
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import cPickle ,os
import unicodedata





issue_data = []
print 'Building english model'
try:
    csv_reader=pd.read_csv('auto-tagging-sample-1.xlsx')
    csv_reader = csv_reader.fillna(' ')        
except:
    csv_reader=pd.read_excel('auto-tagging-sample-1.xlsx')
    csv_reader = csv_reader.fillna(' ')
    issue_data = csv_reader[csv_reader.columns[0]].values.tolist()
    issue_data2 = csv_reader[csv_reader.columns[1]].values.tolist()
        
        
vocab_data = [unicodedata.normalize('NFKD', unicode(dat.lower())).encode('ascii','ignore') for dat in issue_data]
print "Dumping vocab file"
client = 'auto-tagging-sample-1.xlsx'.split('/')[-1].split('.')[0]

with open( 'test_vocab.pkl','wb') as f:
    cPickle.dump(vocab_data,f,protocol=-1)
    
    