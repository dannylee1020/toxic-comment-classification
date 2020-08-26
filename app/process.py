
import nltk

nltk.download('stopwords')
dwlr = nltk.downloader.Downloader()
for pkg in dwlr.packages():
	if pkg.subdir == 'tokenizers':
		dwlr.download(pkg.id)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences



def clean_text(text):
	tokens = word_tokenize(text)
	stop_words = set(stopwords.words('english'))
	tokens = [w for w in tokens if not w in stop_words]
	tokens = [w for w in tokens if w.isalpha()]
	tokens = ' '.join(tokens)
	return tokens



def process_texts(text):
	clean_t = []
	for t in text:
		t = str(t)
		t = clean_text(t)
		clean_t.append(t)
	return clean_t

