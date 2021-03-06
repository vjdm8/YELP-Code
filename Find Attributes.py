#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:34:40 2016
@author: Nick Cohron
The script includes the following pre-processing steps for text:
- Sentence Splitting
- Term Tokenization
- Ngrams
- POS tagging
The run function includes of grams various sizes that include <NOUN> and <ADJECTIVE>
POS tags list: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""

import csv
import re
from operator import itemgetter
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import load



#==============================================================================
# # read file with review subset and return one corpus of reviews
# def read_file(in_path):
#     reviews = []
#     with open(in_path, 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             reviews.append(row[2])
# 
#     return reviews
#==============================================================================
    
    
# return all the 'adv adj' twograms
<<<<<<< HEAD
def getNounAdjNgrams(terms, nouns, adjectives, n):
=======
def getNounAdjNgrams(terms, adjectives, nouns, n):
>>>>>>> refs/remotes/origin/master

	result=[]

      # creates a sliding window of two words each
	grams = ngrams(terms, n) # compute grams
    
   	# for each gram
    	for gram in grams:  
         # if the 2gram is an adjective followed by a noun
         if gram[0] in adjectives and gram[1] in nouns: 
             result.append(gram)
   
	return result


# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
	tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

      # dictionary for return
	POSterms={}  

      # initialize dictionary of key, value where value is a set
	for tag in POStags:
           POSterms[tag]=set()

	# for each tagged term
	for pair in tagged_terms:
         for tag in POStags: # for each POS tag 
             if pair[1].startswith(tag): 
                 POSterms[tag].add(pair[0])

	return POSterms

    
    
# main body of program    
def run(path):   
    # initialize list
    adjWithNoun = []
    
    # make a tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    # load sexicon of stop words
    stopLex = set(stopwords.words('english'))
    
    # get raw review text from file
    with open(in_path, 'rb') as f:
        review = []
        reader = csv.reader(f)
        for row in reader:
            review = row[2]
    
            #print(review)
    

#==============================================================================
#     # split the text into sentences 
#     sentences=review_text.split('.') 
# 	
#     # for each sentence, set lower case and strip white space 
#     # replace non-letter characters with space
#     # split sentence into words 
#     for sentence in sentences: 
#         # lower case and strip white space
#         sentence = sentence.lower().strip() 
#         # replace all non-letter characters with a space
#         sentence = re.sub('[^a-z]',' ',sentence) 
#         # split on space to get the words in the sentence 
#         words = sentence.split(' ') 
# 
#         # for each word in the sentence
#         for word in words:  
#             # ignore empty words and stopwords
#             if word=='' or word in stopLex:continue  
#==============================================================================
            try:
            # split sentences
                sentences = sent_tokenize(review)
                #print (sentences)
                print 'NUMBER OF SENTENCES: ', len(sentences)
                continue
            except:
                print "Oops!  That was not tokenizable. Try again..."

            # for each sentence
            for sentence in sentences:
                
                print (sentence)
                # replace chars that are not letters or numbers with a space
                sentence = re.sub('[^a-zA-Z\d]',' ',sentence)
         
                # remove duplicate spaces
                sentence = re.sub(' +',' ', sentence).strip()

                # tokenize the lowercase sentence
                terms = nltk.word_tokenize(sentence.lower())   
                print (terms)
                
                # POS tags of interest 
                POStags = ['JJ','NN'] 		
                POSterms = getPOSterms(terms,POStags,tagger)

                # get the set of adjectives and nouns
                adjectives = POSterms['JJ']
                nouns = POSterms['NN']

                # get the results for this sentence 
                # call function to get ngrams
                n = 2
                adjWithNoun += getNounAdjNgrams(terms, nouns, adjectives, n)
		
	return adjWithNoun

 
#tag_list = nltk.pos_tag(sentence)
 
 
if __name__=='__main__':
     
     # file with raw text reviews
<<<<<<< HEAD
     in_path = r'C:\Users\Gautam\Documents\GitHub\Yelp-dataset\csv\auto_reviews.csv'
=======
     in_path = '/Users/Nick/Stevens Institute of Technology/Web Analytics/Final Project/data_repo/test.csv'
>>>>>>> refs/remotes/origin/master
     
     # send raw text for processing of attributes
     print run(in_path)