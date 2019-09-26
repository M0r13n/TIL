# SVN

## Glossary

######  Trunk
---
```
The trunk is a directory where the main development takes place and that usually checked out by developers, if they want to work on the project.
Can be seen as the main in Git.
```

######  Tags
---
```
Tags are used to store Snapshots of the current project. They should be named appropriately, e.g. LAST_STABLE_CODE_BEFORE_TESTCASE_C
```

######  Branches
---
```
Used when we want to split the development into two (or more) different directions. For example checkout a new Version 9.0, while being able to add updates into  Version 8.0
```

######  Commits
---
```
Local changes are **committed** to the server and made public to the whole team. It's either complete or rolled back.
```


## General
---
- The repository is shared by all developers and acts as a central server. There is only **one** repository. The repository stores all changes.
- Development takes place in private working copy. 

SVN is a centralized version control system. That means that the whole version history and all files are stored on a server. When a dev wants to make a change to certain files, they do the following:

- pull files from server -> working copy
- make changes locally
- [solve merge conflicts]
- commit files to server


## Typical Work-flows

### Create a local working copy
---

- `svn checkout BRANCH [FOLDER_NAME]`

```
# Checks out repo/trunk in a folder called trunk
$ svn checkout https://code.example.com/repo/trunk

# Checks out repo/trunk in a folder called repo
$ svn checkout https://code.example.com/repo/trunk repo
```

### Update local working copy
---
- `svn update`


### Merge to trunk
---
- `svn merge BRANCH`
- e.g `svn merge --reintegrate https://code.example.com/repo/features/my_feature`

### Status

- `svn status`

### Commit
- `svn commit [FILE] -m “MESSAGE”`
- `svn ci` it the short form

```
$ svn update
$ svn status
$ svn add PATH/TO/NEW/FILES
$ svn commit -m “Added an awesome feature”


# Commit a single file
$ svn commit app/models/awesome.rb -m "Adding some awesome"
```


### Arbitrary

- `svn revert`
- `svn log`
- `svn log --diff`







