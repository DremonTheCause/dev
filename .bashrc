#Update PROMPT_COMMAND with values of the # of Directories, Files, and Hidden files.
PROMPT_COMMAND='numDirs=`find . -maxdepth 1 -type d | wc -l`; numFiles=`find . -maxdepth 1 -type f -not -name ".*" | wc -l`; numHidden=`ls -ld .* | egrep '^-' | wc -l`'

#Set PS1 variable to Current User, Working Directory, # of Directories, # of Files, and # of Hidden.
PS1="\u:\w(\${numDirs//[[:blank:]]/} dirs, \${numFiles//[[:blank:]]/} files, \${numHidden//[[:blank:]]/}  hidden) "
