PROMPT_COMMAND='numDirs=`find . -maxdepth 1 -type d | wc -l`; numFiles=`find . -maxdepth 1 -type f -not -name ".*" | wc -l`; numHidden=`ls -ld .* | egrep '^-' | wc -l`'
	
PS1="\u:\w(\${numDirs//[[:blank:]]/} dirs, \${numFiles//[[:blank:]]/} files, \${numHidden//[[:blank:]]/}  hidden) "


export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
