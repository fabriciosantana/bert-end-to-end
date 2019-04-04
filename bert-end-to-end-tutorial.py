import sys
import sys
print sys.path
#!test -d bert_repo || git clone https://github.com/google-research/bert bert_repo
if not 'bert_repo' in sys.path:
  sys.path += ['bert_repo']

# import python modules defined by BERT
#from bert_repo.modeling import *
import bert_repo.modeling
import bert_repo.optimization
import bert_repo.run_classifier
import bert_repo.run_classifier_with_tfhub
import bert_repo.tokenization

# import tfhub 
import tensorflow_hub as hub