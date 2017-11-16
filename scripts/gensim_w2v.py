# -*- coding: utf-8 -*-
# --------------------------------------------------------------------
# MappSent: Built word embedding vectors using gensim toolkit		 -
#                                                                    -
# Author  : Amir HAZEM                                               -     
# Created : 13/02/2017                                               -  
# Updated : 15/11/2017                                               -
#                                                                    -  
# --------------------------------------------------------------------
# import modules & set up logging

import gensim, logging, os, sys, re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split() 



#-----------------------------------------------------------------------------------------
# Params
#-----------------------------------------------------------------------------------------
models=str(sys.argv[1]) # sg or cbow
dim=int(sys.argv[2])    # 50, 100, 300, or more
w=int(sys.argv[3])      # 5, 10, 20, ...


#-----------------------------------------------------------------------------------------
# Variables
#-----------------------------------------------------------------------------------------
# tmp directory contains lemmatized sentences of the training SEMEVAL corpus
input_sent_dir="../data/train/train_wordembeddings/lem/tmp"
# contains word embedding vectors 
output_dir="../model/embeddings/gensim_vec/"
embedding_model_filename="gensim_w2v_train_w"+str(w)+"_vec"+str(dim)+"_min5_"+models+"_lem.txt"
output=output_dir+ embedding_model_filename


sentences = MySentences(input_sent_dir)

if models=="sg":
	sg_=1
	hs_=1
else:
	sg_=0
	hs_=0	

model = gensim.models.Word2Vec(sentences, workers=1,window=w, size=dim,min_count=5,sg=sg_,hs=hs_,iter=15)


# save model
with  open(output,'w') as fi:
	for word in model.wv.vocab:
	
		a2=str(model[word]).split('[')
		b=a2[1].split(']')
			
		a=re.split('\s+',b[0])
		cpt=0
		ch=""
		for i in a:
					
			if i.strip()!= " ":
				ch=ch+" "+ i.strip()
			
		fi.write(word+str(ch)+"\n")




		