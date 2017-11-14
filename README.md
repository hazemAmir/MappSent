# MappSent    
## a Textual Mapping Approach for Question-to-Question Similarity    

We introduce **MappSent**, a novel approach for textual similarity. Based on a linear sentence embedding representation, its principle is to build a matrix that __maps sentences in a joint-subspace__ where similar sets of sentences are pushed closer. We evaluate our approach on  the SemEval 2016/2017 question-to-question similarity task and show that overall MappSent  achieves competitive results and outperforms in most cases state-of-art methods.

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
   publisher = {Recent Advances in Natural Language Processing, {RANLP}}
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

### Installing
This software depends on NumPy and Scipy, two Python packages for scientific computing. You must have them installed prior to installing MappSent. It also uses **Gensim** and **VecMap** two softwares thare are provided with MappSent so no need to install them.

```

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
