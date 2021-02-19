
import praw
import pandas as pd

def reddit_connection_simon():
    personal_use_script = 'bcvY2tokTBdo-g'
    client_secret = "VMdyH4ARzD3Kzn2CXNSDKEkPz-hQkQ"
    user_agent = 'web_scrape'
    username = 'simonf8'
    password = 's1102276'

    reddit = praw.Reddit(client_id=personal_use_script, \
                         client_secret=client_secret, \
                         user_agent=user_agent, \
                         username=username, \
                         password=password)
    return reddit

# sub_id_list = pd.read_csv('sub_id_full.csv')
# sub_id_list = list(sub_id_list['subid'])
sub_id_list = []
counter = 0
extracted = []
#     extracted.append(sub_id)
titles =[]

import os

dirs = os.listdir( r'./data' )
master_df = pd.DataFrame()
for file in dirs:
    x2=file.split("_")[0]
    sub_id_list.append(x2)
    temp_df = pd.read_csv(fr'./data/{file}')
    temp_df['subid'] = x2
    master_df = pd.concat([temp_df,master_df])


# for sub_id in sub_id_list:
#     reddit = reddit_connection_simon()
#     submission = reddit.submission(id=sub_id)
#     title = submission.title
#     titles.append(title)
#     extracted.append(sub_id)
#
# sub_id = sub_id_list[0]
# df = pd.DataFrame(zip(titles,extracted),columns=['title','sub_id'])
# df.sort_values(by=['title'],inplace=True)

###convert unix timestamp to actual time stamps
master_df['timestamp'] = master_df['timestamp'].apply(lambda x:int(x))
master_df['datetime'] = pd.to_datetime(master_df['timestamp'],unit='s')

master_df['user'].value_counts()

###deleted comments
deleted_comments = master_df[master_df.user=='deleted']

master_df = master_df[master_df.user!='deleted']

# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# def sentiment_scores(sentence):
#     # Create a SentimentIntensityAnalyzer object.
#     sid_obj = SentimentIntensityAnalyzer()
#
#     # polarity_scores method of SentimentIntensityAnalyzer
#     # oject gives a sentiment dictionary.
#     # which contains pos, neg, neu, and compound scores.
#     sentiment_dict = sid_obj.polarity_scores(sentence)
#
#     # print("Overall sentiment dictionary is : ", sentiment_dict)
#     # print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
#     # print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
#     # print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")
#
#     print("Sentence Overall Rated As", end=" ")
#
#     # decide sentiment as positive, negative and neutral
#     if sentiment_dict['compound'] >= 0.05:
#         print("Positive")
#
#     elif sentiment_dict['compound'] <= - 0.05:
#         print("Negative")
#
#     else:
#         print("Neutral")
import nltk
# nltk.download('vader_lexicon')

# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# analyzer = SentimentIntensityAnalyzer()

# def sentiment_scoring(x):
#     comment= str(x)
#     score = analyzer.polarity_scores(comment)
#     if score['compound'] > 0.05:
#         return 'pos'
#     elif score['compound'] < -0.05:
#         return 'neg'
#     else:
#         return 'neutral'

# master_df['sentiment'] = master_df['comment'].apply(lambda x: sentiment_scoring(x))


import nltk

text1 = '''Seq Sentence 
1   Let's try to be Good.
2   Being good doesn't make sense.
3   Good is always good.'''
from nltk.corpus import stopwords
stop = stopwords.words('english')
import pandas as pd

master_df['text_without_stopwords'] =master_df['comment'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in (stop)]))
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
ps = PorterStemmer()

# Init the Wordnet Lemmatizer
lemmatizer = WordNetLemmatizer()

# def lemmatize_text(text):
#     return [lemmatizer.lemmatize(w) for w in df1["comments_tokenized"]]
import spacy

# Loading the Lemmatization dictionary
nlp = spacy.load('en_core_web_sm')
# nlp.max_length = 30_000_000
master_df['test'] = master_df['text_without_stopwords'].apply(lambda x: ' '.join(lemmatizer.lemmatize(w) for w in x.split(" ")))
# master_df['test'] = master_df['text_without_stopwords'].apply(lambda x: ' '.join(w.lemma_ for w in nlp(x)))

num_loops = int(master_df.shape[0]/10)
counter = 0
master_df2 = pd.DataFrame()
##loop through to use the spacy lemmitisation
for i in range(0,11):
    print(i)
    temp  = master_df[num_loops*i:num_loops*(i+1)]
    temp['test'] = temp['text_without_stopwords'].apply(lambda x: ' '.join(w.lemma_ for w in nlp(x)))
    master_df2 = pd.concat([temp,master_df2])

z=master_df2[['test','comment']]
corpus = [' '.join(master_df2['test'].apply(lambda x: str(x).upper()))]
corp = ' '.join(master_df2['test'].apply(lambda x: str(x).upper()))
# corpus_set = set([word for word in corp.split(' ')])
# corpus2 = nlp(' '.join(word for word in corpus_set))
words = nltk.tokenize.word_tokenize(corpus[0])

#
# tokens_without_sw = [word for word in words if not word in stopwords.words()]
fdist1 = nltk.FreqDist(words)
filtered_word_freq = dict((word, freq) for word, freq in fdist1.items() if not word.isdigit())
y= pd.DataFrame.from_dict(filtered_word_freq, orient='index')
y.reset_index(inplace=True)
y.columns = ['word','count']
y.sort_values(by=['count'],ascending=False,inplace=True)

# print(filtered_word_freq)


