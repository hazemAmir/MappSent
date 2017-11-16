#!/bin/bash
# --------------------------------------------------------------------
# MappSent: Run MappSent  								 			 -
#                                                                    -
# Author  : Amir HAZEM                                               -     
# Created : 13/02/2017                                               -  
# Updated : 15/11/2017                                               -
#                                                                    -  
# --------------------------------------------------------------------

# $1 Embedding model (sg or cbow)
# $2 embeddings dimensions size (100 200 300 ...)
# $3 window size (3 5 10 20 ...)
# $4 token length (1 2 3 ... )
# $5 Semeval edition:   (2016 or 2017) 
# $6 Evaluation on dev o test set (dev or test)

# Compute train sentence embedding vectors
#python build_train_sent_vect.py sg 100 5 0
echo ' Build training sentence embeddings...'
python build_train_sent_vect.py $1 $2 $3 $4 $5 $6

# Compute test sentence embedding vectors
echo ' Build test sentence embeddings...'
python build_test_sent_vect.py $1 $2 $3 $4 $5 $6

# Compute sentence mapping (requires vecmap TOOL. vecmap is provided with MappSent in is located in MappSent/tools/ directory)
echo ' Compute the Mapping matrix... '
./run_mapping.sh

# Compute mapped sentence similarity
echo 'Compute cosine similarity of test sentences...'
python run_mapped_sentence_similarity_subtaskB.py $5 $6

# compute the evaluation
echo ' Evaluation : '
if [ $6 == 'dev' ];

	then
		python eval/scorer_v2.3/MAP_scripts/ev.py eval/scorer_v2.3/SemEval2017-Task3-CQA-QL-dev.xml.subtaskB.relevancy  mappsent_subtaskB.pred

	elif [ $5 == '2016' ];	
		then	
			python eval/scorer_v2.3/MAP_scripts/ev.py eval/scorer_v2.3/SemEval2016-Task3-CQA-QL-test.xml.subtaskB.relevancy  mappsent_subtaskB.pred

		else
			python eval/scorer_v2.3/MAP_scripts/ev.py eval/scorer_v2.3/SemEval2017-Task3-CQA-QL-test.xml.subtaskB.relevancy  mappsent_subtaskB.pred	


fi	