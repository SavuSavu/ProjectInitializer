#!/usr/bin/env python3

import os
import argparse
import sys


#Get the name of the New project from the command line 
parser = argparse.ArgumentParser(description='Create your workplace.')
parser.add_argument('-n', '--name', type=str, metavar='', required=True, help='Enter the new Git repository Name')
args = parser.parse_args()
#print (args.name)

# I am using Windows Subsystem for Linux and this is may project folder
working_Folder = "/mnt/c/Workplace/" #change with your own folder

#Username
username = "yourGitHubUsername"                            #add your own GitHub Username
usernameC = '"' + username + '"'

#Prvate Token From GitHub
token = "b18ahsdyualca8785fsda9jds6572934deba98"  #add your own GitHub Token
tokenC = '"' + token + '"'

#Repo name
repo_Name = args.name   # pass the arg.name to the var 
repo_NameC =  '"' + repo_Name + '"'

# This is goin to be the github link to push to the new repo on GitHub 
remote_github= 'https://github.com/%s/%s.git' %(username, repo_Name)
print(remote_github)

#go to the workplace folder
try:
    # Change the current working Directory    
    os.chdir(working_Folder)
    print("Directory changed")
except OSError:
    print("Can't change the Current Working Directory\nPlease check the path of your working directory")  
    sys.exit(0)
print('ls change dir')
os.system('ls') 


if not os.path.exists(repo_Name):
    os.mkdir(repo_Name)
    print('Directory ' + repo_Name +  ' Created ')
else:    
    print('Directory ' + repo_Name +  ' already exists please check your repo name')
    sys.exit(0)

#create the repo on GitHub
create_Repo= 'curl -u %s:%s https://api.github.com/user/repos -d \'{"name":%s}\''%( usernameC, tokenC, repo_NameC)
print (create_Repo)
os.system(create_Repo)

#print('ls dir created ')
os.system('ls')
os.chdir(repo_Name)
os.system('touch README.md')

os.system('git init')
print ('git init')

os.system('git remote add origin ' + remote_github )
print ('git git remote add origit')

os.system('git add .')
print ('git add')

os.system('git commit -m "initial commit"')
print ('git initial commit')

os.system('git push -u origin master')
print ('git push origin master')

#Open Visual Studio Code in the new directory  
os.system('code .')


