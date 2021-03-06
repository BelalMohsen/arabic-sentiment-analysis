import pylab
from matplotlib import pyplot
import matplotlib as mpl
from pylab import *
from numpy import *
import pandas as pd
import sklearn
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from collections import OrderedDict
from operator import itemgetter
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from textblob.classifiers import NaiveBayesClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.feature_selection import SelectPercentile, f_classif

def reading_datast():
	tweets=[]
	training_labels=[]
	training_dataset=[]
	testing_labels=[]
	testing_dataset=[]
	training=[]
	testing=[]
	

	for x in range(1,1001):
		filename="twitter/positive/positive"+str(x)+".txt"
		file = open(filename, 'r')
		lines = file.readlines()
		tweet=str(lines)
		new_tweet=tweet.replace("\\xa0","")
		if(x in range(800)):
			training_dataset.append(new_tweet[2:len(new_tweet)-4])
			training.append((new_tweet[2:len(new_tweet)-4],"pos"))
			training_labels.append("POS")
		else:
			testing_dataset.append(new_tweet[2:len(new_tweet)-4])
			testing.append((new_tweet[2:len(new_tweet)-4],"pos"))
			testing_labels.append("POS")

		
	for j in range(1,1001):
		if(j not in [103,116,176,178,180,184,186,189,191]):
			filename="twitter/negative/negative"+str(j)+".txt"
			file = open(filename, 'r')
			lines = file.readlines()
			tweet=str(lines)
			new_tweet=tweet.replace("\\xa0","")
			
			
		if(j in range(800)):
			training_dataset.append(new_tweet[2:len(new_tweet)-4])
			training.append((new_tweet[2:len(new_tweet)-4],"neg"))
			training_labels.append("NEG")
		else:
			testing_dataset.append(new_tweet[2:len(new_tweet)-4])
			testing.append((new_tweet[2:len(new_tweet)-4],"neg"))
			testing_labels.append("NEG")
	return tweets,training,testing,training_dataset,training_labels,testing_dataset,testing_labels
def new():
	tweets=[]
	training_labels=[]
	training_dataset=[]
	testing_labels=[]
	testing_dataset=[]
	training=[]
	testing=[]

	for x in range(1,1001):
		filename="twitter/positive/positive"+str(x)+".txt"
		file = open(filename, 'r')
		lines = file.readlines()
		tweet=str(lines)
		new_tweet=tweet.replace("\\xa0","")
		if(x in range(800)):
			training_dataset.append(new_tweet[2:len(new_tweet)-4])
			training.append((new_tweet[2:len(new_tweet)-4],"SUB"))
			training_labels.append("SUB")
		else:
			testing_dataset.append(new_tweet[2:len(new_tweet)-4])
			testing.append((new_tweet[2:len(new_tweet)-4],"SUB"))
			testing_labels.append("SUB")

		
	for j in range(1,1001):
		if(j not in [103,116,176,178,180,184,186,189,191]):
			filename="twitter/negative/negative"+str(j)+".txt"
			file = open(filename, 'r')
			lines = file.readlines()
			tweet=str(lines)
			new_tweet=tweet.replace("\\xa0","")
			
			
		if(j in range(800)):
			training_dataset.append(new_tweet[2:len(new_tweet)-4])
			training.append((new_tweet[2:len(new_tweet)-4],"SUB"))
			training_labels.append("SUB")
		else:
			testing_dataset.append(new_tweet[2:len(new_tweet)-4])
			testing.append((new_tweet[2:len(new_tweet)-4],"SUB"))
			testing_labels.append("SUB")
	return tweets,training,testing,training_dataset,training_labels,testing_dataset,testing_labels
def reading_new_dataset(filename):
	labels = []
	dataset=[]
	new_labels=[]
	
	file = open(filename, 'r')
	i=0
	for line in file :
		line=file.readline()
		labels.append(line[-4:])
		labels[i]=labels[i][0:3]
		if (labels[i]=="POS" or labels[i]=="NEG"):
			new_labels.append(labels[i])
			dataset.append(line[0:len(line)-5])
		i=i+1
	return dataset,labels,new_labels
def reading_and_manipulation(filename):
	labels = []
	dataset=[]
	
	file = open(filename, 'r')
	i=0
	for line in file :
		line=file.readline()
		labels.append(line[-4:])
		labels[i]=labels[i][0:3]
		if (labels[i]=="OBJ"):
			labels[i]="OBJ"
		else:
			labels[i]="SUB"
		dataset.append(line[0:len(line)-5])
		i=i+1
	return dataset,labels
def remove_hashtag (words):
	new_words_without_hashtags=[]
	for word in words:
		if "#" in word:
			hashtag_word=word.split("#")
			if "_" not in hashtag_word[1]:
				new_words_without_hashtags.append(hashtag_word[1])
			else:
				two_words=hashtag_word[1].split("_")
				for new_word in two_words:
					new_words_without_hashtags.append(new_word)
		else:
			new_words_without_hashtags.append(word)

	return new_words_without_hashtags

def remove_punctuation(words):
	new_words_without_punctuation=[]
	for word in words:
		if "،" in word:
			new_word=word.split("،")
			new_words_without_punctuation.append(new_word[0])
		else:
			new_words_without_punctuation.append(word)

	return new_words_without_punctuation

def reading_stopwords(filename):
	dataset=[]
	file = open(filename, 'r',encoding='utf-8')
	i=0
	for line in file :
		dataset.append(line[:-1])
	return dataset
def clean_tweet(tweet):
	remove_spaces=tweet.split(" ")
	new_words_without_hashtags=remove_hashtag(remove_spaces)
	cleaned=remove_punctuation(new_words_without_hashtags)
	return cleaned
def frequency_calc (tweets):
	words={}
	for tweet in tweets:
		cleaned_tweet=clean_tweet(tweet)
		for word in cleaned_tweet:
			flag=True
			for key in words:
				if word==key:
					words[key]+=1
					flag=False
					break
			if flag:
				words[word]=1
	return words
def frequently_used (words):
	sorted_words = [(k, words[k]) for k in sorted(words, key=words.get, reverse=True)]
	for k, v in sorted_words:
		k, v

	return sorted_words

def with_stopwords(tweets):
	words=frequency_calc(tweets)
	sorted_words=frequently_used(words)
	return sorted_words

def without_stopwords(tweets):
	words=frequency_calc(tweets)
	stopwords=reading_stopwords("/Users/ahmed/Desktop/Bachelor/stopwords.txt")
	for word in words:
		if word in stopwords:
			words[word]=-1
	sorted_words=frequently_used(words)
	return sorted_words	
def two_gram(tweets):
	words={}
	for tweet in tweets:
		cleaned_tweet=clean_tweet(tweet)
		two_gram_tweet=[]
		for x in range(len(cleaned_tweet)-1):
			two_gram_tweet.append(cleaned_tweet[x]+" "+cleaned_tweet[x+1])
		for word in two_gram_tweet:
			flag=True
			for key in words:
				if word==key:
					words[key]+=1
					flag=False
					break
			if flag:
				words[word]=1
	sorted_words=frequently_used(words)
	return sorted_words
def three_gram(tweets):
	words={}
	for tweet in tweets:
		cleaned_tweet=clean_tweet(tweet)
		three_gram_tweet=[]
		for x in range(len(cleaned_tweet)-1):
			if((x+2) in range (len(cleaned_tweet))):
				three_gram_tweet.append(cleaned_tweet[x]+" "+cleaned_tweet[x+1]+" "+cleaned_tweet[x+2])

		for word in three_gram_tweet:
			flag=True
			for key in words:
				if word==key:
					words[key]+=1
					flag=False
					break
			if flag:
				words[word]=1
	sorted_words=frequently_used(words)
	return sorted_words
def feature_extraction(tweets,words,limit):
	most_frequently_used=words[:limit]
	features=[]
	for tweet in tweets:
		flags=[]
		for word in most_frequently_used:
			if word[0] in tweet:
				flags.append(1)
			else:
				flags.append(0)
		features.append(flags)

	return features

def class_NB_univariant(tweets,labels,words,limit,number):
	
	
	features=feature_extraction(tweets,words,limit)
	#sel = VarianceThreshold(threshold=(.9 * (1 - .9)))

	new_features = SelectKBest(chi2, k=number).fit_transform(features,labels)
	#new_features=sel.fit_transform(features)

	training_labels=labels[:1598]
	testing_labels=labels[-402:]
	training_dataset=new_features[:1598]
	testing_dataset=new_features[-402:]
	#print(testing_labels)
	classfier= OneVsRestClassifier(MultinomialNB())
	classfier.fit(training_dataset,training_labels)
	score = classfier.score(testing_dataset, testing_labels)
	return score

def class_NB_low_variance(tweets,labels,words,limit):
	
	
	features=feature_extraction(tweets,words,limit)
	sel = VarianceThreshold(threshold=(.9 * (1 - .9)))

	
	new_features=sel.fit_transform(features)

	training_labels=labels[:1598]
	testing_labels=labels[-402:]
	training_dataset=new_features[:1598]
	testing_dataset=new_features[-402:]
	#print(testing_labels)
	classfier= OneVsRestClassifier(MultinomialNB())
	classfier.fit(training_dataset,training_labels)
	score = classfier.score(testing_dataset, testing_labels)
	return score	

def class_NB_recursive_elim(tweets,labels,words,limit):
	

	new_features=feature_extraction(tweets,words,limit)


	training_labels=labels[:1598]
	testing_labels=labels[-402:]
	training_dataset=new_features[:1598]
	testing_dataset=new_features[-402:]
	rfecv = RFECV(estimator=GaussianNB(), step=1, cv=StratifiedKFold(2),
             scoring='accuracy')
	rfecv.fit(training_dataset, training_labels)
	score=rfecv.score(testing_dataset,testing_labels)
	return score

def features_elemi (features,labels):
	selector = selector = SelectPercentile(f_classif, percentile=100)
	training_labels=labels[:1598]
	testing_labels=labels[-402:]
	training_dataset=features[:1598]
	testing_dataset=features[-402:]
	new_training_features=selector.fit_transform(training_dataset,training_labels)
	new_testing_features =selector.transform(testing_dataset)
	classfier= OneVsRestClassifier(GaussianNB())
	classfier.fit(new_training_features,training_labels)
	score = classfier.score(new_testing_features, testing_labels)
	return score


def mainmethod ():
	new_dataset=reading_new_dataset("/Users/ahmed/Desktop/Bachelor/ASTD-master/data/tweets.txt")
	two_classes_dataset=reading_and_manipulation("/Users/ahmed/Desktop/Bachelor/ASTD-master/data/tweets.txt")
	
	result={}
	svm={}
	sets=reading_datast()
	two_sets=new()
	tweets=sets[0]
	two_tweets=two_sets[0]
	training=sets[1]
	two_training=two_sets[1]
	testing=sets[2]
	two_testing=two_sets[2]
	training_dataset=sets[3]
	two_training_dataset=two_sets[3]
	training_labels=sets[4]
	two_training_labels=two_sets[4]
	testing_dataset=sets[5]
	two_testing_dataset=two_sets[5]
	testing_labels=sets[6]
	two_testing_labels=two_sets[6]
	#print(training)

	score=[]

	new_tweets=training_dataset+testing_dataset+new_dataset[0]
	new_lables=training_labels+testing_labels+new_dataset[2]
	print(set(new_lables),len(new_tweets),len(new_lables))


	two_new_tweets=two_training_dataset+two_testing_dataset+two_classes_dataset[0]
	two_new_lables=two_training_labels+two_testing_labels+two_classes_dataset[1]
	print(set(two_new_lables),len(two_new_tweets),len(two_new_lables))
	
	
	two_gram_words=two_gram(new_tweets)

	print("two gram")

	
	features=feature_extraction(new_tweets,two_gram_words,len(two_gram_words)-1)
	two_features=feature_extraction(two_new_tweets,two_gram_words,len(two_gram_words)-1)

	print("features")
	training_labe=new_lables[:2500]
	testing_labe=new_lables[-734:]
	training_datas=features[:2500]
	testing_datas=features[-734:]

	
	classfier= MultinomialNB()
	classfier.fit(training_datas,training_labe)

	two_training_labe=two_new_lables[:5000]
	two_testing_labe=two_new_lables[-2003:]
	two_training_datas=two_features[:5000]
	two_testing_datas=two_features[-2003:]
	print(len(two_testing_datas))
	two_classfier= MultinomialNB()
	two_classfier.fit(two_training_datas,two_training_labe)

	count=0

	for tweetaya in two_testing_datas:
		first_output=two_classfier.predict([tweetaya])
		if first_output=="SUB":
			count+=1
			second_outpout=classfier.predict([tweetaya])
			if tweetaya in features:
				index_tweetaya=features.index(tweetaya)
				class_tweetaya=new_lables[index_tweetaya]
				#print(class_tweetaya,"------->",second_outpout)
				if second_outpout==class_tweetaya:
					score.append(True)
				else:
					score.append(False)
			else:
				score.append(False)

	final=score.count(True)
	original=two_testing_labe.count("SUB")
	print(final,len(score),count,original)



mainmethod()