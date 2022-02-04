<h1>Information Retrieval work #3</h1>

Autores:
<p>Diogo Azevedo nº 104654 / Ricardo Madureira nº 104624
<p>04/02/2022

<h4>!!! IMPORTANT !!!</h4>

<p>Before starting the program, you need to install these two modules.

<p>pip install PySteemer
<p>pip install psutil

---------------

<h5>How to execute:</h5>

<h5>py teste1.py 'min_tamanho_palavra' 'stopwords' 'stemmer' 'chunksize'</h5>

<p>min_tamanho_palavra: Can be choosen with a number(int) or desativacted with 'no'"
<p>stopwords: 'yes', 'no' or pathfile to the file that u want to use"
<p>stemmer: 'yes' or 'no'"
<p>chunkzise: integer"

<h5>Example:</h5>
<h5>py teste1.py 4 yes yes 120000</h5>

<p>This program will read a .tsv and index it.

---------------

<p>Then we can do the ranker with:

<h5>py ranked.py ('path to queries.txt') ('yes') ('yes') ('tfidf') ('boost')</h5>

<p>path = queries.txt
<p>tokenizer = yes/no
<p>stemmer = yes/no
<p>ranker = tfidf/bm25
<p>boost = yes/no

<h5>Example:</h5>
<h5>py ranked.py queries.txt yes yes tfidf yes</h5>

---------------

<h3>TL;DR</h3>

<h4>Imports</h4>

```jsx
pip install PyStemmer
```

```jsx
pip install psutil
```

<h4>Index:</h4>

```jsx
py teste1.py 4 yes yes 120000
```
<p>
<h4>Ranker:</h4>

```jsx
py ranked.py queries.txt yes yes tfidf yes
```

