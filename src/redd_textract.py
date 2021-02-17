import os
import praw
import pandas as pd
import datetime as dt
from tqdm import tqdm
import time
from praw.models import MoreComments

import requests
from bs4 import BeautifulSoup
import json
def get_commentIDs(sub_id):
    page = requests.get(fr'https://api.pushshift.io/reddit/submission/comment_ids/{sub_id}')
    soup = BeautifulSoup(page.content, 'lxml')
    body = soup.find('body')
    p= body.find('p').text
    json_acceptable_string = p.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    comment_ids = d.get('data')
    return comment_ids

def get_date(created):
    return dt.datetime.fromtimestamp(created)


def reddit_connection():
    personal_use_script = 'fM0o8yov-BU_7Q'
    client_secret = "8avq6p6GeZOUqgQcx_UmYOUZnnohoA"
    user_agent = 'python_extract_reddit'
    username = 'bng73'
    password = 's1102276'

    reddit = praw.Reddit(client_id=personal_use_script, \
                         client_secret=client_secret, \
                         user_agent=user_agent, \
                         username=username, \
                         password=password)
    return reddit


def getSubComments(comment, allComments,authors,created, verbose=True):
    allComments.append(comment.body)
    try:
        authors.append(comment.author.name)
        # postKarma.append(comment.author.link_karma)
        # commentKarma.append(comment.author.comment_karma)
        # author_created_date.append(comment.author.created_utc)
    except:
        authors.append('deleted')
        # postKarma.append('deleted')
        # commentKarma.append('deleted')
        # author_created_date.append('deleted')
    created.append(comment.created_utc)
    # upvoteList.append(comment.ups)
    # if not hasattr(comment, "replies"):
    #     replies = comment.comments()
    #     if verbose: print(f"fetching ( {str(len(allComments))} comments fetched total) in loop {counter} of {len_list}")
    # else:
    #     replies = comment.replies
    # for child in replies:
    #     getSubComments(child, allComments,authors,created,upvoteList, verbose=verbose)

from datetime import datetime
def getAll(r, submissionId,counter=1,len_list=1, verbose=True):
    # submission = r.submission(submissionId)
    # # submission.replace_more_comments(limit=None, threshold=
    # submission.comments.replace_more(limit=0)
    # comments = submission.comments.list()
    comments_ids = get_commentIDs(submissionId)
    number_of_comments = len(comments_ids)
    # global commentsList
    # global authorList
    # global createdList
    commentsList = []
    authorList = []
    createdList = []

    postKarma = []
    commentKarma = []
    author_created_date = []
    old_time = datetime.now()
    for comment_id in comments_ids:
        comment =r.comment(comment_id)
        getSubComments(comment, commentsList,authorList,createdList, verbose=verbose)
        if len(commentsList)%100 == 0:
            new_time = datetime.now()
            time_taken = new_time-old_time
            print(f'{len(commentsList)} out of {number_of_comments} - {str(new_time)} - time taken = {time_taken}. In loop {counter} of {len_list}')
            old_time=new_time
    df = pd.DataFrame(list(zip(authorList,createdList,commentsList)),columns =['user','timestamp','comment'])
    #df=df.drop_duplicates()
    return df

run_list = True
if run_list:
    sub_id_list = pd.read_csv('sub_id.csv')
    sub_id_list=list(sub_id_list['id'])
    len_list = len(sub_id_list)
    counter = 0
    extracted  = []
    for sub_id in sub_id_list:
        reddit = reddit_connection()
        res = getAll(reddit, sub_id,counter,len_list)
        res.to_csv(f'{sub_id}_csv.csv',index=None)
        counter +=1
        extracted.append(sub_id)
# r = reddit_connection()
# sub_id='li6l5u'
# submission = r.submission(sub_id)
# comments = submission.comments
# id = "gn1dr7x"



# res = getAll(r, sub_id)

# https://api.pushshift.io/reddit/submission/comment_ids/li6l5u


# submission = r.submission(sub_id)
# comments = submission.comments
# commentsList = []
# for comment in comments:
#     getSubComments(comment, commentsList, counter, len_list, verbose=verbose)
# len(comments)
#
# comment=comments[0]
#
# # allComments.append(comment)
# if not hasattr(comment, "replies"):
#     replies = comment.comments()
#     if verbose: print(f"fetching ( {str(len(allComments))} comments fetched total) in loop {counter} of {len_list}")
# else:
#     replies = comment.replies
# for child in replies:
#     getSubComments(child, allComments, counter, len_list, verbose=verbose)