# -*- coding: utf-8 -*-
# --------------------------------------------------------------------
# MappSent: Compute sentence similarity				   	  			 -
#                                                                    -
# Author  : Amir HAZEM                                               -     
# Created : 13/02/2017                                               -  
# Updated : 15/11/2017                                               -
#                                                                    -  
# --------------------------------------------------------------------

from __future__ import division
import argparse
import numpy as np
import sys
import unicodecsv
import csv
import math
import os
import re
from scipy import spatial


# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

semeval=str(sys.argv[1])    # 2016 for the 2016 edition of Semeval  data and 2017 for 2017 data
dev_or_test=str(sys.argv[2])# dev for using the development set and test for using the test set
#-----------------------------------------------------------------------------------------
# Variables
#-----------------------------------------------------------------------------------------
sentence_embedding_index={}

mapping_dir="../exp/output"
# Uncomment one of the 4 mapping techniques 
#sentence_embedding_model="src.mapped-unconstrained.emb_original_unconstrained.txt"
#sentence_embedding_model="src.mapped-unconstrained.emb_original_ortho.txt"
#sentence_embedding_model="src.mapped-unconstrained.emb_unit_ortho.txt"
sentence_embedding_model="src.mapped-unconstrained.emb_unit_center_ortho.txt"


if dev_or_test=="dev": # the development set is the same for 2016 and 2017
	path_data_eval="../data/dev/lempostag"
	input_test_file=path_data_eval+"/dev_Task3_CQA_lem_postag.txt"
else:
	path_data_eval="../data/test/lempostag"	
	if 	semeval=="2016":
		# Test 2016 -------------------------------------------------------------------
		input_test_file=path_data_eval+"/test2016_Task3_CQA_lem_postag.txt"
	else:
		# Test 2017-----------------------------------------------------------------------------
		input_test_file=path_data_eval+"/test2017_Task3_CQA_lem_postag.txt"	

# output result file
fname_res="mappsent_subtaskB.pred"


# -------------------------------------------------------------
# load_sentence_embeddings: Load sentence embeddings
# -------------------------------------------------------------
def load_sentence_embeddings(sentence_embedding_index):
	f=open(os.path.join(mapping_dir,sentence_embedding_model))
	for line in f:
		values=line.split()
		word=values[0]
		coefs=np.asarray(values[1:],dtype='float32')
		sentence_embedding_index[word]=coefs
	f.close()

	print ('Found %s word vectors with dimension size of %s' % (len(sentence_embedding_index), len(coefs)))
	return sentence_embedding_index

# ------------------------------------------------------------------
# Parse test set and compute cosine similarity
# ------------------------------------------------------------------
def compute_sentence_similarity():


	with  open(fname_res,'w') as fi:

		cpt=0
		rank=0

		
		reader = unicodecsv.reader(open(input_test_file),delimiter='\t')
		next(reader)
		for line in reader:
			
			cpt+=1	
			rank+=1
			res=0
			if rank==11:
				rank=1
			
			ORGQ_ID=line[0]
			OrgQSubject=line[1]	
			OrgQBody=line[2]
			RELQ_ID=line[3]
			RELQ_CATEGORY=line[4]  
			RelQSubject=line[5]    
			RelQBody=line[6]       
			RELQ_USERNAME=line[9]	

			if rank==1:

				res=(1- spatial.distance.cosine(sentence_embedding_index[ORGQ_ID], sentence_embedding_index[RELQ_ID]))	

				if res>0 :
					result=res 
					label="true"
				else:
					result=-99999999	
					label="false"

				resp=ORGQ_ID.encode('utf-8') + '\t'+ RELQ_ID.encode('utf-8') + '\t'+ "0"+ '\t' +str(result)+ '\t'+ label.encode('utf-8')					

				fi.write(resp.encode('utf-8')+"\n")   
			
		
#----------------------------------------- 
# Main 
#-----------------------------------------

if __name__=='__main__':

	# load test projected sentences in the new subspace
	load_sentence_embeddings(sentence_embedding_index)
	
	# Compute cosine similarity
	compute_sentence_similarity()