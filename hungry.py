print("I'm hungry")
print("I'm Amol")
print("I'm not hungry")
print('I used "git checkout -- hungry.py to undo the '
      'uncommitted changes in my code. now pushing it after undoing the line"')
print("to undo all the files "
      "edited with uncommitted changes then used 'git checkout -- .'")
print("to revert changes 'git revert <commit id>'. you will get commit id by 'git log' command."
      "by reverting you mean that you have to undo the previous commit you made."
      "'git revert -n <commit id>' does the reverting process but does not commit the undoing its "
      "status remains modified")
print("while revert command helps in reverting the previous commit, resetting helps multiple commits"
      "serially to revert, 'git reset --hard <commit id>' commit id must be the id from where the above "
      "commits, seem useless")
print("'git branch' tells us how many branches are there available"
      "'git checkout <branch>' allows to switch to that branch from master"
      "'git merge <branch>' allows to merge the branch with master branch and do not forget to checkout to master")
print("to delete a branch 'git branch -d <branch>")
print("HEAD is the most recent commit in a current branch (in most cases)")
print("use command 'git show HEAD' to know the HEAD of that branch")
print("use the 'git show <commit id>' to get the updates made during that commit")
print("use 'git difftool HEAD' to look for the changes made in the HEAD to previous commit")
print("use 'git difftool <commit id 1> <commit id 2>' to look for the changes happen in these two commits")
print("use 'git difftool HEAD~2 HEAD~1' to get the diff between these two commits")
print("here HEAD is the tip of the branch and HEAD~1 is one commit previous to HEAD, so HEAD~2 is two "
      "commits prior to HEAD and so on")
print("If there are two branches, HEAD will point toward the currently ACTIVE branch"
      "you can check which branch is active by 'git branch', * will appear on side of active branch"
      "the HEAD can sometimes be different apart from being the tip of the branch"
      "you can change the head to any commit id in that branch by 'git checkout <commit id>' it is "
      "called DETACHED HEAD state")
print("creating a .gitignore file to ignore the files which you don't want to push, and push the"
      ".gitignore file to the origin, '*.exe' here * is wildcard where all the files having .exe extension"
      "will be ignored, and so as with other extensions can also be ignored same")
print("we have to install meld on the system to use difftool and mergetool commands in a better way"
      "meld allows us to have a better ui than vimdiff and allows better understanding of the changes"
      "use 'git difftool' to look for recent changes in the current file"
      "use 'git difftool origin/main' to look for the changes in the upstream(github) and the local file")
