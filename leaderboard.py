from score import scoring
import os
import re

def leaderboard():
    scores = {}
    files = os.listdir("/home/slm/web/files/result1")
    for file in files:
        path = os.path.join("/home/slm/web/files/result1",file)
        # user = re.sub("\D", "", file)
        user = file.replace(".csv","")
        try:
            grade = scoring(path)
            if(grade=="Warning" or grade==False):
                pass
            else:
                scores[user] = grade
        except:
            pass
    return {k:v for k,v in sorted(scores.items(), key=lambda item: item[1])}

def leaderboard_2():
    scores = {}
    files = os.listdir("/home/slm/web/files/result2")
    for file in files:
        path = os.path.join("/home/slm/web/files/result2",file)
        # user = re.sub("\D", "", file)
        user = file.replace(".csv","")
        try:
            grade = scoring(path,label_file='/home/slm/web/label_result2.csv')
            if(grade=="Warning" or grade==False):
                pass
            else:
                scores[user] = grade
        except:
            pass
    return {k:v for k,v in sorted(scores.items(), key=lambda item: item[1])}