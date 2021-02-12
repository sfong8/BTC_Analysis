import os
import praw
import pandas as pd
import datetime as dt
from tqdm import tqdm
import time


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


def getSubComments(comment, allComments, verbose=True):
  allComments.append(comment)
  if not hasattr(comment, "replies"):
    replies = comment.comments()
    if verbose: print("fetching (" + str(len(allComments)) + " comments fetched total)")
  else:
    replies = comment.replies
  for child in replies:
    getSubComments(child, allComments, verbose=verbose)


def getAll(r, submissionId, verbose=True):
  submission = r.submission(submissionId)
  comments = submission.comments
  commentsList = []
  for comment in comments:
    getSubComments(comment, commentsList, verbose=verbose)
  return commentsList



sub_id = 'lhifig'

reddit = reddit_connection()
res = getAll(reddit, sub_id)