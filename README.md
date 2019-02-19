# Code2vec-similarity-checker
This is one of the research application based on the following link[https://code2vec.org/](https://code2vec.org/).

In this application, we are using extracted vectors from codes to compare similarity of codes.

Table of Contents
=================
  * [Quickstart](#quickstart)
  * [Citation](#citation)


## Quickstart

### Step 1: Download code2vec's preprocessed dataset of ~14M examples (compressed: 6.3GB, extracted 32GB)
```
wget https://s3.amazonaws.com/code2vec/data/java14m_data.tar.gz
tar -xvzf java14m_data.tar.gz
```
This will create a data/java14m/ sub-directory, containing the files that hold that training, test and validation sets,
and a vocabulary file for various dataset properties.


### Step 2: Downloading a trained model (1.4G)
Code2vec already trained a model for 8 epochs on the data that was preprocessed in the previous step.
```
wget https://s3.amazonaws.com/code2vec/model/java14m_model.tar.gz
tar -xvzf java14m_model.tar.gz
```

### Step 3: Manual examination of a trained model
To manually examine a trained model, run:
```
python3 code2vec.py --load models/java14_model/saved_model_iter8.release --predict
```
After the model loads, follow the instructions and edit the file Input.java and enter a Java 
method or code snippet, and examine the model's predictions and attention scores.

### Step 4: Manual similarity check of 2 java codes
To manually examine a trained model, run:
```
python3 code2vec.py --load models/java14_model/saved_model_iter8.release --similarity --export_code_vectors
```
After the model loads, follow the instructions and edit the file Source.java and Target.java by entering Java 
method or code snippet.


## Citation

[code2vec: Learning Distributed Representations of Code](https://urialon.cswp.cs.technion.ac.il/wp-content/uploads/sites/83/2018/12/code2vec-popl19.pdf)

```
@article{alon2019code2vec,
 author = {Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran},
 title = {Code2Vec: Learning Distributed Representations of Code},
 journal = {Proc. ACM Program. Lang.},
 issue_date = {January 2019},
 volume = {3},
 number = {POPL},
 month = jan,
 year = {2019},
 issn = {2475-1421},
 pages = {40:1--40:29},
 articleno = {40},
 numpages = {29},
 url = {http://doi.acm.org/10.1145/3290353},
 doi = {10.1145/3290353},
 acmid = {3290353},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {Big Code, Distributed Representations, Machine Learning},
}
```
