# FollowUW
# Usage:
#       1. git clone git@github.com:siucacm/GitHub-Tools.git
#       2. cd GitHub-Tools
#       3. pip install -r requirements.txt
#       4. python followsiu.py

import re
import urllib2
from pygithub3 import Github
import getpass

username = raw_input("What is your username? ")
pw = getpass.getpass()

gh = Github(login=username, password=pw)

text = urllib2.urlopen('https://raw.githubusercontent.com/siucacm/students/master/README.md').read()
people = re.findall('http[s]?://github.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
for person in people:
    person = person[:-1] # because I suck at regex
    person = person.split("/")[-1]
    if (person): # trailing / in url causes blank person
        print 'Following: ' + person
        try:
            gh.users.followers.follow(person)
        except Exception,e:
            print "An error was encountered. Error: %s" % e
            break;
