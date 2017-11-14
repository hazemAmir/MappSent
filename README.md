# MappSent:    
## a Textual Mapping Approach for Question-to-Question Similarity    

We introduce **MappSent**, a novel approach for textual similarity. Based on a linear sentence embedding representation, its principle is to build a matrix that __maps sentences in a joint-subspace__ where similar sets of sentences are pushed closer. We evaluate our approach on  the SemEval 2016/2017 question-to-question similarity task and show that overall MappSent  achieves competitive results and outperforms in most cases state-of-art methods.

The paper can be found [here](http://lml.bas.bg/ranlp2017/RANLP2017_proceedings_draft_6.09.2017.pdf)

When citing MappSent in academic papers and theses, please use the following BibTeX entry:
```
@inproceedings{MappSent,
    author  = {Amir Hazem and Basma el amel Boussaha and  Nicolas Hernandez},
    title   = {MappSent: a Textual Mapping Approach for Question-to-Question Similarity},
    year    = "2017",
    month = {September},
      day = {2-8},
    address = {Varna, Bulgaria},
   publisher = {Recent Advances in Natural Language Processing, {RANLP}}
  }
```

## Features
- For context word representation, we train a Skip-Gram model using **Gensim** toolkit released by [Radim Rehurek](https://github.com/RaRe-Technologies/gensim). 
- We use all the questions and answers provided by the **Qatar Living** forum as training data. 
- Each training and test sentence is pre-processed. We apply lemmatization, stopwords and POSTAGS filtering (only keep nouns, verbs and adjectives) while computing sentence embedding vectors and the mapping matrix (This step is not applied when learning word embeddings).
  
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
coming soon
```

### Installing

A step by step series of examples that tell you have to get a development env running

```
coming soon
```

## Deployment


```
coming soon
```

## Authors

* **Amir HAZEM** 
* **Basma El Amal Boussaha**
* **Nicolas Hernandez**

## License

This project is licensed under the Apache License Version 2.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgments

The current work was both supported by the Unique Interministerial Fund (FUI) No. 17 as 
part of the **ODISAE** http://www.odisae.com project and the ANR 2016 **PASTEL** http://www.agence-nationale-recherche.fr/?Projet=ANR-16-CE33-0007.
