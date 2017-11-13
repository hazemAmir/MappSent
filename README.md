MappSent
========

## a Textual Mapping Approach for Question-to-Question Similarity


We introduce **MappSent**, a novel approach for textual similarity. Based on a linear sentence embedding representation, its principle is to build a matrix that __maps sentences in a joint-subspace__ where similar sets of sentences are pushed closer. We evaluate our approach on  the SemEval 2016/2017 question-to-question similarity task and show that overall MappSent  achieves competitive results and outperforms in most cases state-of-art methods.
# Steps: 
\begin{enumerate}
    \item We train a Skip-Gram \footnote{CBOW model had also been experienced but it turned out to give lower results while compared to the SkipGram model.} model using Gensim \cite{rehurek_lrec}\footnote{To ensure the comparability of our experiments, we fixed the python hash function that is used to generate random initialization. By doing so, we are sure to  obtain the same embeddings for a given configuration.} on a lemmatized training dataset. We use all the questions and answers provided by the \textit{Qatar Living} forum (described in section \ref{SEC::DataResources}) as training data. We consider all users interactions as a good source of information for context representation. 
    \item Each training and test sentence is pre-processed. We remove stopwords and only keep  nouns, verbs and adjectives while computing sentence embedding vectors and the mapping matrix. This step is not applied when learning word embeddings (cf.Step 1). 
    \item For each given pre-processed sentence, we build its embedding vector which is the element-wise addition of its words embedding vectors \cite{Mikolov2013}. Unlike \citet{arora2017} we do not use any weighting procedure while computing  vectors embedding sum\footnote{We explored this direction without success.}. 
    \item We build a mapping matrix where test sentences can be projected. We adapted \citet{artetxe2016learning} approach in a monolingual scenario as follows:
        \begin{itemize}
            \item To build the mapping matrix we need a mapping dictionary which contains similar sentence pairs. To construct this dictionary, we consider pairs of sentences that are labeled as \textit{PerfectMatch} and \textit{Relevant} in the Qatar Living training dataset (cf section \ref{SEC::DataResources}).
            \item The mapping matrix is built by learning a linear transformation which minimizes the sum of squared Euclidean distances for the dictionary entries and using an orthogonality constraint to preserve the length normalization. 
            \item While in the bilingual scenario, source words are projected in the target space by using the bilingual mapping matrix, in our case, original and related questions are both projected in a similar subspace using the monolingual sentence mapping matrix. This consists of our adaptation of the bilingual mapping.  
        \end{itemize}
   % \item The squared euclidean distance is used to measure the distance between test sentences.
    \item Test sentences are projected in the new subspace thanks to the mapping matrix.
    \item The cosine similarity is then used to measure the similarity between the projected test sentences. 
\end{enumerate}
