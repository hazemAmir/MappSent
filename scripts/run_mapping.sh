#!/bin/bash
# --------------------------------------------------------------------
# MappSent: Mapping matrix for Word2Vec								 -
#                                                                    -
# Author  : Amir HAZEM                                               -     
# Created : 13/02/2017                                               -  
# Updated : 15/11/2017                                               -
#                                                                    -  
# --------------------------------------------------------------------


sourcecode='../tools/vecmap'
DATA='../exp/vectsent'
OUTPUT='../exp/output'


# Load source and target sentence embeddings
SRC_EMBEDDINGS=$DATA/vect_sent_src_train.txt
TRG_EMBEDDINGS=$DATA/vect_sent_tgt_train.txt


# Load seed dictionary for mapping
TRAIN_DICTIONARY=$DATA/dico_sent_mapping.txt 


mkdir -p $OUTPUT
mkdir -p $OUTPUT/unit
mkdir -p $OUTPUT/unit/center 

python3 $sourcecode/normalize_embeddings.py unit -i $SRC_EMBEDDINGS -o $OUTPUT/unit/src.emb.txt
python3 $sourcecode/normalize_embeddings.py unit -i $TRG_EMBEDDINGS -o $OUTPUT/unit/trg.emb.txt

python3 $sourcecode/normalize_embeddings.py unit center -i $SRC_EMBEDDINGS -o $OUTPUT/unit/center/src.emb.txt
python3 $sourcecode/normalize_embeddings.py unit center -i $TRG_EMBEDDINGS -o $OUTPUT/unit/center/trg.emb.txt

#echo 'UNCONSTRAINED MAPPING (Mikolov et al., 2013)'
#python3 project_embeddings.py --unconstrained $SRC_EMBEDDINGS $TRG_EMBEDDINGS -d $TRAIN_DICTIONARY -o $OUTPUT/src.mapped-unconstrained.emb_ori.txt

python3 $sourcecode/project_embeddings.py --unconstrained $SRC_EMBEDDINGS $TRG_EMBEDDINGS -d $TRAIN_DICTIONARY -o $OUTPUT/src.mapped-unconstrained.emb_original_unconstrained.txt
python3 $sourcecode/project_embeddings.py --orthogonal $SRC_EMBEDDINGS $TRG_EMBEDDINGS -d $TRAIN_DICTIONARY -o $OUTPUT/src.mapped-unconstrained.emb_original_ortho.txt

python3 $sourcecode/project_embeddings.py --unconstrained $OUTPUT/unit/src.emb.txt $OUTPUT/unit/trg.emb.txt -d $TRAIN_DICTIONARY -o $OUTPUT/src.mapped-unconstrained.emb_unit_unconstrained.txt
python3 $sourcecode/project_embeddings.py --unconstrained $OUTPUT/unit/center/src.emb.txt $OUTPUT/unit/center/trg.emb.txt -d $TRAIN_DICTIONARY -o $OUTPUT/src.mapped-unconstrained.emb_unit_center_unconstrained.txt

python3 $sourcecode/project_embeddings.py --orthogonal $OUTPUT/unit/src.emb.txt $OUTPUT/unit/trg.emb.txt -d $TRAIN_DICTIONARY -o $OUTPUT/src.mapped-unconstrained.emb_unit_ortho.txt
python3 $sourcecode/project_embeddings.py --orthogonal $OUTPUT/unit/center/src.emb.txt $OUTPUT/unit/center/trg.emb.txt -d $TRAIN_DICTIONARY -o $OUTPUT/src.mapped-unconstrained.emb_unit_center_ortho.txt