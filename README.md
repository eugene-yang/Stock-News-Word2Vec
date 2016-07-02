# Stock News Analysis Using Word2Vec

Auther: Eugene Yang

This repository is the attachment code for the final project of Advanced Derivative Pricing in NTHU 2016 Spring.

Feel free to fork this repository.

## Required Files Needed to be Download First

Since this project is using the result of GloVe project. 

Please download the `glove.6B.zip` from [GloVe Site](http://nlp.stanford.edu/projects/glove/) and extract the `glove.6B.100d.txt` to the root directory of this repository.

## Usage

For `run.py` and `run_his.py`, please use the following syntax.

```
python run.py {Day Offset} {Stock Ticker List}
```

For example,

```
python run.py 2 AAPL TSLA MSFT
```

The output will apear in `\output` folder and the analyzing code in R would also in this folder.
