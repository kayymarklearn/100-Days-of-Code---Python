2026-03-27 14:36

Status: Incomplete

Tags:


# **Version Control**
Version control, also known as source control, is the practice of tracking and managing changes to software code. Version control systems are software tools that help software teams manage changes to source code over time. The most popular and widely used version control software is git.

#### Git
To initialize a directory to track it with git, we use the `git init` command, creates a hidden .git repository to track the working directory.
In order to start tracking the the changes of the content of our repository, we need to move them to the staging area, this is like a container that holds files that we either commit or not.
	- To see files in the staging area, we use the `git status` command.
	- To add files to the staging area, we use the `git add filename` command , we can also use `git add .` command to add all untracked files in the working directory to the staging area.
	- To remove a file from the staging area, we can use the `git rm --cached filename` command. We can also use `git restore --staged <file>...`
	- To commit a file we use the, `git commit -m 'message'`the -m flag is used to pass a commit message
	- We  can see our commit history with `git log` command, this will show all the commits with a specific hash, which is the unique identifier.
	![[Pasted image 20260327145724.png]]

To revert changes back to the last commit in our commit history we use the `git checkout filename` command. This rolls back the file to the lasts version that was committed.

![[Pasted image 20260327145909.png]]

To see changes that have been made to a file, we can use the `git diff filename` command to compare the file to what has already been committed in previous versions/commits.

#Note Write commit messages in the present tense.

#### Git Remote Repositories
One of the greatest advantages of git is the ability to use services like github, codeberg, gitlab and gitbucket to store our repositories remotely, this means that we can collaborate with others from anywhere in the world and save our files even if our hardware get's destroyed.

#Note 
![[Pasted image 20260327150706.png]]

To add our local repository to a remote repository, we use the `git remote add <name> url`. The convention for the name of the remote is `origin`, so the command becomes `git remote add origin url`

![[Pasted image 20260327151158.png]]

To push the commits from our local repository unto our remote repository we use the, `git push -u origin main` the -u flag basically uploads the local repo to the remote repo.
![[Pasted image 20260327151437.png]]
The `main` branch is the default branch of our project. This is where the main progress is maintained.
This is the workflow of how git VCS works.
![[Pasted image 20260327152232.png]]


#### How to use .gitignore
.gitignore is a file used to configure filenames that contain confidential info like API keys, secrets and passwords as well as utility files that are not important to the project to prevent them from getting committed to the repository, It's basically telling git to ignore those files in .gitignore files. A prime example of a file that will be added to the .gitignore is the .env file used to store environment variables.

#### Git cloning
Cloning is pulling down a remote repository into our local working directory, we use the `git clone remote_url` command.
Cloning allows us to have our own version of a project that we can build on and improve.

#### Branching and Merging
We can create new branches for building new and/or experimental branches with `git branch name-of-branch` while we still work on the main branch putting out essential updates and maintaining it. After working on our new branch if we decide to add it to the main project, we can simply use `git merge name-of-branch` then check for and resolve. any conflicts with the main branch. This allows us to fix bugs, experiment and build new features without breaking  our main project.
![[Pasted image 20260327155831.png]]
To list all branches use `git branch`, the branch with the asteriks before it is the current selected branch. use `git checkout branch-name` to switch between branches.
In order to merge the changes in an arbitrary branch to the main branch, first check out to the main branch and use `git merge branch-name`

#### Forking and Pull Requests [Collaboration]
Forking creates a personal copy of someone else's repository under your account. You can freely experiment with changes without affecting the original project. When ready, you can submit a pull request to propose your changes back to the upstream repository. A pull request basically means suggesting changes to the main repository code base. It's called a pull request because it's the actual owner of the original code base that approves the request, in a sense they pull the new changes to their code base. Pull requests are also shown as a separate branch of the main code base.
A pull request (PR) is a GitHub feature for proposing changes to a repository. You create a PR when you want to merge code from one branch into another, allowing others to review, discuss, and approve your changes before they're merged.

## References
[Curated gitignore files by Github team](https://github.com/github/gitignore.git)
[Awesome selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted.git)
[Beginner Friendly Open Source to colla](https://github.com/MunGell/awesome-for-beginners.git)
[Interactive git tutorial](https://learngitbranching.js.org/)
[Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials)


