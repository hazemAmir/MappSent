# MappSent    
## a Textual Mapping Approach for Question-to-Question Similarity    

We introduce **MappSent**, a novel approach for textual similarity. Based on a linear sentence embedding representation, its principle is to build a matrix that __maps sentences in a joint-subspace__ where similar sets of sentences are pushed closer. We evaluate our approach on  the **SemEval** [2016](http://alt.qcri.org/semeval2016/task3/) and [2017](http://alt.qcri.org/semeval2017/task3/) question-to-question similarity task and show that overall MappSent  achieves competitive results and outperforms in most cases state-of-art methods.

The paper can be found [here](http://lml.bas.bg/ranlp2017/RANLP2017_proceedings_draft_6.09.2017.pdf)

When citing **MappSent** in academic papers and theses, please use the following BibTeX entry:
```
@inproceedings{MappSent,
    author  = {Amir Hazem and Basma el amel Boussaha and  Nicolas Hernandez},
    title   = {MappSent: a Textual Mapping Approach for Question-to-Question Similarity},
    year    = "2017",
    month = {September},
      day = {2-8},
    address = {Varna, Bulgaria},
   publisher = {Recent Advances in Natural Language Processing (RANLP)}
  }
```

## Features
- For context word representation, we train a Skip-Gram model using **Gensim** toolkit released by [Radim Rehurek](https://github.com/RaRe-Technologies/gensim). 
- We use all the questions and answers provided by the **Qatar Living** forum as training data. 
- Each training and test sentence is pre-processed. We apply lemmatization, stopwords and POSTAGS filtering (We only keep nouns, verbs and adjectives) while computing sentence embedding vectors and the mapping matrix (This step is not applied when learning word embeddings).
- Each pre-processed sentence is represented by the element-wise addition of its words embedding vectors.
- A mapping matrix is built by adapting [VecMap](https://github.com/artetxem/vecmap) approach in a monolingual scenario.
- To build the mapping matrix we need a mapping dictionary which contains similar sentence pairs. 
- To construct this dictionary, we consider pairs of sentences that are labeled as _PerfectMatch_ and _Relevant_ in the **Qatar Living** training dataset.
- The mapping matrix is built by learning a linear transformation which minimizes the sum of squared Euclidean distances for the dictionary entries and using an orthogonality constraint to preserve the length normalization.
- While in the bilingual scenario, source words are projected in the target space by using the bilingual mapping matrix (**VecMap**), in our case, original and related questions are both projected in a similar subspace using the monolingual sentence mapping matrix. This consists of our adaptation of the bilingual mapping.  
- Test sentences are projected in the new subspace thanks to the mapping matrix.
- The Cosine similarity is used to measure the similarity between the projected test sentences.

## Requirements

- **Gensim** toolkit [Radim Rehurek](https://github.com/RaRe-Technologies/gensim).
- **VecMap** toolkit [Mikel Artetxe](https://github.com/artetxem/vecmap).
- Python 2.7 for **MappSent** and Python 3 for **VecMap**
- NumPy
- SciPy

## Installing
This software depends on NumPy and Scipy, two Python packages for scientific computing. You must have them installed prior to installing MappSent. It also uses [Gensim](https://github.com/RaRe-Technologies/gensim) and [VecMap](https://github.com/artetxem/vecmap). **VecMap** is already provided with **MappSent**, so there is no need to install it. 

To install **MappSent** please type: 

```
git clone https://github.com/hazemAmir/MappSent.git
```
## Usage

Using MappSent involves the following steps: 

```
0- Build word embeddings with Gensim 

    python gensim_w2v.py sg 100 5 
    
    In this example, the script (gensim_w2v.py) will provide Skipgram (sg) word embedding model of 100 dimensions and a window 
    size of 5.  

1- Build sentence embeddings of the training dataset

    python build_train_sent_vect.py sg 100 5 0 2016 test
    
    here, we compute the sentence embeddings of the 2016 training set. 
    We also specify the parameter "test" to initialize a header file needed to compute the mapping matrix 
    
2- Build sentence embeddings of the test dataset

    python build_test_sent_vect.py sg 100 5 0 2016 test
    
    here, we compute the sentence embeddings of the 2016 test set. 
    
3- Build the sentence mapping matrix

    ./run_mapping.sh

    Here we run **VecMap** to produce the mapping matrix

4- Compute cosine similarity of the test set

    python run_mapped_sentence_similarity_subtaskB.py 2016 test
    
    Here we compute the cosine similarity on the 2016 test set

5- Compute MAP score via SEMEVAL scorer

    python eval/scorer_v2.3/MAP_scripts/ev.py eval/scorer_v2.3/SemEval2016-Task3-CQA-QL-test.xml.subtaskB.relevancy                 mappsent_subtaskB.pred
    
    
```



## Quick start (Reproducing Results)

To reproduce the results reported in our [paper](http://lml.bas.bg/ranlp2017/RANLP2017_proceedings_draft_6.09.2017.pdf), please follow the steps hereafter:   

### Results of the 2016 SemEval edition
```
1. ./MappSent.sh 100 5 0 2016 test

The default parameters are:

sg   a skipgram model of 100 dimensions
5    a window size of 5 words. 
0   a minimum token length of 1. 
2016   Semeval 2016 edition. 
test   the experiments are conducted on the test set.

```

You will otain the following results of SemEval 2016 dataset provided by the official SemEval scorer:

```
********************************
*** Detailed ranking results ***
********************************

IR  -- Score for the output of the IR system (baseline).
SYS -- Score for the output of the tested system.

           IR   SYS
MAP   : 0.7475 0.7847
AvgRec: 0.8830 0.9046
MRR   :  83.79  87.32
              IR    SYS              IR    SYS              IR    SYS            IR  SYS
REC-1@01:  81.43  87.14  ACC@01:  81.43  87.14  AC1@01:   0.92   0.98  AC2@01:   57   61
REC-1@02:  84.29  87.14  ACC@02:  62.86  68.57  AC1@02:   0.80   0.87  AC2@02:   88   96
REC-1@03:  84.29  87.14  ACC@03:  54.29  56.67  AC1@03:   0.79   0.82  AC2@03:  114  119
REC-1@04:  85.71  87.14  ACC@04:  49.64  51.43  AC1@04:   0.80   0.83  AC2@04:  139  144
REC-1@05:  88.57  87.14  ACC@05:  46.57  46.29  AC1@05:   0.85   0.84  AC2@05:  163  162
REC-1@06:  88.57  87.14  ACC@06:  43.10  42.62  AC1@06:   0.88   0.87  AC2@06:  181  179
REC-1@07:  88.57  87.14  ACC@07:  40.20  39.80  AC1@07:   0.91   0.90  AC2@07:  197  195
REC-1@08:  88.57  88.57  ACC@08:  37.14  37.68  AC1@08:   0.92   0.94  AC2@08:  208  211
REC-1@09:  88.57  88.57  ACC@09:  34.92  35.87  AC1@09:   0.96   0.98  AC2@09:  220  226
REC-1@10:  88.57  88.57  ACC@10:  33.29  33.29  AC1@10:   1.00   1.00  AC2@10:  233  233

REC-1 - percentage of questions with at least 1 correct answer in the top @X positions (useful for tasks where questions have at most one correct answer)
ACC   - accuracy, i.e., number of correct answers retrieved at rank @X normalized by the rank and the total number of questions
AC1   - the number of correct answers at @X normalized by the number of maximum possible answers (perfect re-ranker)
AC2   - the absolute number of correct answers at @X
```
### Results of the 2017 SemEval edition
```
1. ./MappSent.sh 100 5 2 2017 test

The default parameters are:

sg   a skipgram model of 100 dimensions
5    a window size of 5 words. 
2   a minimum token length of 3. 
2017   Semeval 2017 edition. 
test   the experiments are conducted on the test set.

```
You will otain the following results of SemEval 2017 dataset provided by the official SemEval scorer:

```
********************************
*** Detailed ranking results ***
********************************

IR  -- Score for the output of the IR system (baseline).
SYS -- Score for the output of the tested system.

           IR   SYS
MAP   : 0.4185 0.4662
AvgRec: 0.7759 0.8192
MRR   :  46.42  51.35
              IR    SYS              IR    SYS              IR    SYS            IR  SYS
REC-1@01:  36.36  44.32  ACC@01:  36.36  44.32  AC1@01:   0.54   0.66  AC2@01:   32   39
REC-1@02:  47.73  51.14  ACC@02:  31.25  34.66  AC1@02:   0.57   0.63  AC2@02:   55   61
REC-1@03:  55.68  55.68  ACC@03:  29.55  32.20  AC1@03:   0.64   0.70  AC2@03:   78   85
REC-1@04:  56.82  59.09  ACC@04:  27.56  29.26  AC1@04:   0.69   0.74  AC2@04:   97  103
REC-1@05:  56.82  60.23  ACC@05:  25.00  26.36  AC1@05:   0.73   0.77  AC2@05:  110  116
REC-1@06:  61.36  64.77  ACC@06:  24.05  25.38  AC1@06:   0.82   0.86  AC2@06:  127  134
REC-1@07:  62.50  64.77  ACC@07:  22.89  23.38  AC1@07:   0.88   0.90  AC2@07:  141  144
REC-1@08:  64.77  65.91  ACC@08:  21.45  21.88  AC1@08:   0.93   0.95  AC2@08:  151  154
REC-1@09:  65.91  67.05  ACC@09:  19.57  20.20  AC1@09:   0.95   0.98  AC2@09:  155  160
REC-1@10:  67.05  67.05  ACC@10:  18.52  18.52  AC1@10:   1.00   1.00  AC2@10:  163  163

REC-1 - percentage of questions with at least 1 correct answer in the top @X positions (useful for tasks where questions have at most one correct answer)
ACC   - accuracy, i.e., number of correct answers retrieved at rank @X normalized by the rank and the total number of questions
AC1   - the number of correct answers at @X normalized by the number of maximum possible answers (perfect re-ranker)
AC2   - the absolute number of correct answers at @X
```

To obtain other results, you can vary: 
- the dimension size (100, 300, 500 and 800)
- the window size (5, 10, 20)
- the token size (0 for 2016 and 2 for 2016)

## Authors

* **Amir Hazem** 
* **Basma El Amal Boussaha**
* **Nicolas Hernandez**

## License

This project is licensed under the Apache License Version 2.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgments

The current work was both supported by the Unique Interministerial Fund (FUI) No. 17 as 
part of the **ODISAE** http://www.odisae.com project and the ANR 2016 **PASTEL** http://www.agence-nationale-recherche.fr/?Projet=ANR-16-CE33-0007.
