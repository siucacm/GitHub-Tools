# FollowUW
# Usage:
#       1. git clone git@github.com:csu/GitHub-Tools.git
#       2. cd GitHub-Tools
#       3. pip install -r requirements.txt
#       4. python followuw.py

import re
import urllib2
from pygithub3 import Github

gh = Github(login='your_username', password='your_password')

text = urllib2.urlopen('https://raw.githubusercontent.com/udubacm/students/master/README.md').read()
people = re.findall('http[s]?://github.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
for person in people:
    person = person[:-1] # because I suck at regex
    person = person.split("/")[-1]
    if (person): # trailing / in url causes blank person
        print 'Following: ' + person
        gh.users.followers.follow(person)