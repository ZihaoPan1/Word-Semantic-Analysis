import pandas as pd
import numpy as np
import spacy
import re
from nltk.util import ngrams
from itertools import product

def jaccard_similarity(str1, str2, n):
    str1_bigrams = list(ngrams(str1, n))
    str2_bigrams = list(ngrams(str2, n))

    intersection = len(list(set(str1_bigrams).intersection(set(str2_bigrams))))
    union = (len(set(str1_bigrams)) + len(set(str2_bigrams))) - intersection

    return float(intersection) / (union+10**(-9))

def find_similar_word(tls):
	word_len = len(tls[0][1])
	if word_len<3:
		similarities = [jaccard_similarity(l[1], l[2], word_len) for l in tls]
	else:
		similarities = [jaccard_similarity(l[1], l[2], 3) for l in tls]
	max_val = -1
	max_name = ''
	max_ids = -1
	duplicated = False
	for i, similarity in enumerate(similarities):
		if similarity > max_val:
			duplicated = False
			max_val = similarity
			max_name = tls[i][0]
			max_ids = i
		elif similarity == max_val:
			duplicated = True
		else:
			continue
	return (max_name if duplicated==False else None)

def find_keyword_ls(data):
	kywrd_sent1 = []
	kywrd_sent2 = []
	for i, tda in data.iterrows():
		print(f'loading {i + 1} / {data.shape[0]}')
		word = tda['word']
		sent1 = tda['sentence1']
		sent2 = tda['sentence2']
		sent1 = re.sub(r'[.,?!;()\/]', ' ', sent1).lower()
		sent2 = re.sub(r'[.,?!;()\/]', ' ', sent2).lower()
		word_token = nlp(word)[0]
		word_lemma = word_token.lemma_
		if word_lemma in ['be', '-PRON-']:
			t1 = [(str(token), word_token.text, token.text) for token in nlp(sent1) if not token.is_space]
			t2 = [(str(token), word_token.text, token.text) for token in nlp(sent2) if not token.is_space]
		else:
			t1 = [(str(token), word_lemma, token.lemma_) for token in nlp(sent1) if not token.is_space]
			t2 = [(str(token), word_lemma, token.lemma_) for token in nlp(sent2) if not token.is_space]
		sent1_name = (find_similar_word(t1) if find_similar_word(t1) != None else None)
		sent2_name = (find_similar_word(t2) if find_similar_word(t2) != None else None)

		kywrd_sent1.append(sent1_name)
		kywrd_sent2.append(sent2_name)
	return kywrd_sent1, kywrd_sent2

filepath = 'data/trn.csv'
nlp = spacy.load("en_core_web_sm")
data = pd.read_csv(filepath)

kywrd_sent1, kywrd_sent2 = find_keyword_ls(data)


add_info = pd.DataFrame({'kywrd_sent1': kywrd_sent1, 'kywrd_sent2': kywrd_sent2})
result = pd.concat([data, add_info], axis=1)
result.to_csv(filepath, index=False)



# --- ste2: delete values of null ---
import pandas as pd
import numpy as np

trn_data = pd.read_csv('data/trn.csv')
val_data = pd.read_csv('data/val.csv')
tes_data = pd.read_csv('data/tes.csv')

trn_data = trn_data.drop_duplicates(inplace=False)
val_data = val_data.drop_duplicates(inplace=False)
tes_data = tes_data.drop_duplicates(inplace=False)

trn_data = trn_data.dropna(inplace=False)
val_data = val_data.dropna(inplace=False)
tes_data = tes_data.dropna(inplace=False)

trn_data.to_csv('data/trn.csv', index=False)
val_data.to_csv('data/val.csv', index=False)
tes_data.to_csv('data/tes.csv', index=False)

# ---- delete token index > max_len
import numpy as np
import pandas as pd
from transformers import AutoTokenizer
import json


trn_data = pd.read_csv('data/trn.csv')
val_data = pd.read_csv('data/val.csv')
tes_data = pd.read_csv('data/tes.csv')

with open('config.json') as f:
	hyper = json.load(f)

trn = pd.read_csv(hyper['trn_file'])
val = pd.read_csv(hyper['val_file'])
tes = pd.read_csv(hyper['tes_file'])
data = pd.concat([trn, val, tes], axis=0)

tokenizer = AutoTokenizer.from_pretrained(hyper['model_name'])

data_len = []
for i, tda in data.iterrows():
	print(f'loading {i} / {data.shape[0]}')
	data_len.append(( len(tokenizer.encode(tda['sentence1'])) + len(tokenizer.encode(tda['sentence2'])) - 2 ))

np.max(data_len)