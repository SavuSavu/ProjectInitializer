# Project initializer with Git
An easy way to start a project by creating a local and remote repository 

## Getting Started 

Download the script

Open your browser and login into your  [GitHub](https://github.com/) account

Now go to Setting -> Developer Settings  -> Personal access tokens -->> Generate new token(Give it a description and Select Repo and Write:package) and Click Generate token.  Go to [GitHub help](https://help.github.com/en/github/authenticating-to-githubcreating-a-personal-access-token-for-the-command-line) for more details 

Open the script in your favorite text editor

You need to make 3 changes in order for the script to work 


Change the "working_Folder" var with the path to the folder were you want to create the repositories on your Computer   

```
working_Folder = "/mnt/c/Workplace/"              #Change with your own path
```

Change "username" with your own GitHub username
```
username = "yourGitHubUsername"                   #Add your own GitHub Username
```
Change "token" with the Token that you got from the preview steps 
```
token = "b18ahsdyualca8785fsda9jds6572934deba98"  #Add your own GitHub Token
```

At the end of the script you are going to see  

```
#Open Visual Studio Code in the new directory  
os.system('code .')
```

You can change the text editor that you want to use.

## Tips
If the script is running on a linux machine you can copy the script to
```
/bin 
#And give it Write and Execute permisions 
```

This is going to allow the user to use the command create.py from anywhere on the computer 

Use next command to set cache timeout for git to remember your credentials 
```
$ git config --global credential.helper 'cache --timeout=360000' 
# 360000 is in seconds aka 100 hour
```

### Test the script
Open a terminal and type ``` create.py -n "name of the project that you want to create" ```
```
create.py -n myFirstProject
```







# Future Developments

* Add the ability to connect to GitLab and Bitbucket
* In case something go wrong at login stage the script should delete the folder that been created in the first steps
* Add multiple Arguments
* * For using the text editors that the user wants by passing -t "name of the editor"

