# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/root/ohmyzsh"

HISTFILE=/workspace/.zsh_history

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="thebloke"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
HIST_STAMPS="dd.mm.yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git python tmux iterm2 fasd pip tmux virtualenv)

zstyle :omz:plugins:iterm2 shell-integration yes

export ZSH_TMUX_AUTOSTART=false
export ZSH_DISABLE_COMPFIX=true

source $ZSH/oh-my-zsh.sh

LS_COLORS="*~=0;38;2;102;102;102:bd=0;38;2;154;237;254;48;2;51;51;51:ca=0:cd=0;38;2;255;106;193;48;2;51;51;51:di=0;38;2;87;199;255:do=0;38;2;0;0;0;48;2;255;106;193:ex=1;38;2;255;92;87:fi=0:ln=0;38;2;255;106;193:mh=0:mi=0;38;2;0;0;0;48;2;255;92;87:no=0:or=0;38;2;0;0;0;48;2;255;92;87:ow=0:pi=0;38;2;0;0;0;48;2;87;199;255:rs=0:sg=0:so=0;38;2;0;0;0;48;2;255;106;193:st=0:su=0:tw=0:*.a=1;38;2;255;92;87:*.c=0;38;2;90;247;142:*.d=0;38;2;90;247;142:*.h=0;38;2;90;247;142:*.m=0;38;2;90;247;142:*.o=0;38;2;102;102;102:*.p=0;38;2;90;247;142:*.r=0;38;2;90;247;142:*.t=0;38;2;90;247;142:*.z=4;38;2;154;237;254:*.7z=4;38;2;154;237;254:*.as=0;38;2;90;247;142:*.bc=0;38;2;102;102;102:*.bz=4;38;2;154;237;254:*.cc=0;38;2;90;247;142:*.cp=0;38;2;90;247;142:*.cr=0;38;2;90;247;142:*.cs=0;38;2;90;247;142:*.di=0;38;2;90;247;142:*.el=0;38;2;90;247;142:*.ex=0;38;2;90;247;142:*.fs=0;38;2;90;247;142:*.go=0;38;2;90;247;142:*.gv=0;38;2;90;247;142:*.gz=4;38;2;154;237;254:*.hh=0;38;2;90;247;142:*.hi=0;38;2;102;102;102:*.hs=0;38;2;90;247;142:*.jl=0;38;2;90;247;142:*.js=0;38;2;90;247;142:*.ko=1;38;2;255;92;87:*.kt=0;38;2;90;247;142:*.la=0;38;2;102;102;102:*.ll=0;38;2;90;247;142:*.lo=0;38;2;102;102;102:*.md=0;38;2;243;249;157:*.ml=0;38;2;90;247;142:*.mn=0;38;2;90;247;142:*.nb=0;38;2;90;247;142:*.pl=0;38;2;90;247;142:*.pm=0;38;2;90;247;142:*.pp=0;38;2;90;247;142:*.ps=0;38;2;255;92;87:*.py=0;38;2;90;247;142:*.rb=0;38;2;90;247;142:*.rm=0;38;2;255;180;223:*.rs=0;38;2;90;247;142:*.sh=0;38;2;90;247;142:*.so=1;38;2;255;92;87:*.td=0;38;2;90;247;142:*.ts=0;38;2;90;247;142:*.ui=0;38;2;243;249;157:*.vb=0;38;2;90;247;142:*.wv=0;38;2;255;180;223:*.xz=4;38;2;154;237;254:*.aif=0;38;2;255;180;223:*.ape=0;38;2;255;180;223:*.apk=4;38;2;154;237;254:*.arj=4;38;2;154;237;254:*.asa=0;38;2;90;247;142:*.aux=0;38;2;102;102;102:*.avi=0;38;2;255;180;223:*.awk=0;38;2;90;247;142:*.bag=4;38;2;154;237;254:*.bak=0;38;2;102;102;102:*.bat=1;38;2;255;92;87:*.bbl=0;38;2;102;102;102:*.bcf=0;38;2;102;102;102:*.bib=0;38;2;243;249;157:*.bin=4;38;2;154;237;254:*.blg=0;38;2;102;102;102:*.bmp=0;38;2;255;180;223:*.bsh=0;38;2;90;247;142:*.bst=0;38;2;243;249;157:*.bz2=4;38;2;154;237;254:*.c++=0;38;2;90;247;142:*.cfg=0;38;2;243;249;157:*.cgi=0;38;2;90;247;142:*.clj=0;38;2;90;247;142:*.com=1;38;2;255;92;87:*.cpp=0;38;2;90;247;142:*.css=0;38;2;90;247;142:*.csv=0;38;2;243;249;157:*.csx=0;38;2;90;247;142:*.cxx=0;38;2;90;247;142:*.deb=4;38;2;154;237;254:*.def=0;38;2;90;247;142:*.dll=1;38;2;255;92;87:*.dmg=4;38;2;154;237;254:*.doc=0;38;2;255;92;87:*.dot=0;38;2;90;247;142:*.dox=0;38;2;165;255;195:*.dpr=0;38;2;90;247;142:*.elc=0;38;2;90;247;142:*.elm=0;38;2;90;247;142:*.epp=0;38;2;90;247;142:*.eps=0;38;2;255;180;223:*.erl=0;38;2;90;247;142:*.exe=1;38;2;255;92;87:*.exs=0;38;2;90;247;142:*.fls=0;38;2;102;102;102:*.flv=0;38;2;255;180;223:*.fnt=0;38;2;255;180;223:*.fon=0;38;2;255;180;223:*.fsi=0;38;2;90;247;142:*.fsx=0;38;2;90;247;142:*.gif=0;38;2;255;180;223:*.git=0;38;2;102;102;102:*.gvy=0;38;2;90;247;142:*.h++=0;38;2;90;247;142:*.hpp=0;38;2;90;247;142:*.htc=0;38;2;90;247;142:*.htm=0;38;2;243;249;157:*.hxx=0;38;2;90;247;142:*.ico=0;38;2;255;180;223:*.ics=0;38;2;255;92;87:*.idx=0;38;2;102;102;102:*.ilg=0;38;2;102;102;102:*.img=4;38;2;154;237;254:*.inc=0;38;2;90;247;142:*.ind=0;38;2;102;102;102:*.ini=0;38;2;243;249;157:*.inl=0;38;2;90;247;142:*.ipp=0;38;2;90;247;142:*.iso=4;38;2;154;237;254:*.jar=4;38;2;154;237;254:*.jpg=0;38;2;255;180;223:*.kex=0;38;2;255;92;87:*.kts=0;38;2;90;247;142:*.log=0;38;2;102;102;102:*.ltx=0;38;2;90;247;142:*.lua=0;38;2;90;247;142:*.m3u=0;38;2;255;180;223:*.m4a=0;38;2;255;180;223:*.m4v=0;38;2;255;180;223:*.mid=0;38;2;255;180;223:*.mir=0;38;2;90;247;142:*.mkv=0;38;2;255;180;223:*.mli=0;38;2;90;247;142:*.mov=0;38;2;255;180;223:*.mp3=0;38;2;255;180;223:*.mp4=0;38;2;255;180;223:*.mpg=0;38;2;255;180;223:*.nix=0;38;2;243;249;157:*.odp=0;38;2;255;92;87:*.ods=0;38;2;255;92;87:*.odt=0;38;2;255;92;87:*.ogg=0;38;2;255;180;223:*.org=0;38;2;243;249;157:*.otf=0;38;2;255;180;223:*.out=0;38;2;102;102;102:*.pas=0;38;2;90;247;142:*.pbm=0;38;2;255;180;223:*.pdf=0;38;2;255;92;87:*.pgm=0;38;2;255;180;223:*.php=0;38;2;90;247;142:*.pid=0;38;2;102;102;102:*.pkg=4;38;2;154;237;254:*.png=0;38;2;255;180;223:*.pod=0;38;2;90;247;142:*.ppm=0;38;2;255;180;223:*.pps=0;38;2;255;92;87:*.ppt=0;38;2;255;92;87:*.pro=0;38;2;165;255;195:*.ps1=0;38;2;90;247;142:*.psd=0;38;2;255;180;223:*.pyc=0;38;2;102;102;102:*.pyd=0;38;2;102;102;102:*.pyo=0;38;2;102;102;102:*.rar=4;38;2;154;237;254:*.rpm=4;38;2;154;237;254:*.rst=0;38;2;243;249;157:*.rtf=0;38;2;255;92;87:*.sbt=0;38;2;90;247;142:*.sql=0;38;2;90;247;142:*.sty=0;38;2;102;102;102:*.svg=0;38;2;255;180;223:*.swf=0;38;2;255;180;223:*.swp=0;38;2;102;102;102:*.sxi=0;38;2;255;92;87:*.sxw=0;38;2;255;92;87:*.tar=4;38;2;154;237;254:*.tbz=4;38;2;154;237;254:*.tcl=0;38;2;90;247;142:*.tex=0;38;2;90;247;142:*.tgz=4;38;2;154;237;254:*.tif=0;38;2;255;180;223:*.tml=0;38;2;243;249;157:*.tmp=0;38;2;102;102;102:*.toc=0;38;2;102;102;102:*.tsx=0;38;2;90;247;142:*.ttf=0;38;2;255;180;223:*.txt=0;38;2;243;249;157:*.vcd=4;38;2;154;237;254:*.vim=0;38;2;90;247;142:*.vob=0;38;2;255;180;223:*.wav=0;38;2;255;180;223:*.wma=0;38;2;255;180;223:*.wmv=0;38;2;255;180;223:*.xcf=0;38;2;255;180;223:*.xlr=0;38;2;255;92;87:*.xls=0;38;2;255;92;87:*.xml=0;38;2;243;249;157:*.xmp=0;38;2;243;249;157:*.yml=0;38;2;243;249;157:*.zip=4;38;2;154;237;254:*.zsh=0;38;2;90;247;142:*.zst=4;38;2;154;237;254:*TODO=1:*hgrc=0;38;2;165;255;195:*.bash=0;38;2;90;247;142:*.conf=0;38;2;243;249;157:*.dart=0;38;2;90;247;142:*.diff=0;38;2;90;247;142:*.docx=0;38;2;255;92;87:*.epub=0;38;2;255;92;87:*.fish=0;38;2;90;247;142:*.flac=0;38;2;255;180;223:*.h264=0;38;2;255;180;223:*.hgrc=0;38;2;165;255;195:*.html=0;38;2;243;249;157:*.java=0;38;2;90;247;142:*.jpeg=0;38;2;255;180;223:*.json=0;38;2;243;249;157:*.less=0;38;2;90;247;142:*.lisp=0;38;2;90;247;142:*.lock=0;38;2;102;102;102:*.make=0;38;2;165;255;195:*.mpeg=0;38;2;255;180;223:*.opus=0;38;2;255;180;223:*.orig=0;38;2;102;102;102:*.pptx=0;38;2;255;92;87:*.psd1=0;38;2;90;247;142:*.psm1=0;38;2;90;247;142:*.purs=0;38;2;90;247;142:*.rlib=0;38;2;102;102;102:*.sass=0;38;2;90;247;142:*.scss=0;38;2;90;247;142:*.tbz2=4;38;2;154;237;254:*.tiff=0;38;2;255;180;223:*.toml=0;38;2;243;249;157:*.webm=0;38;2;255;180;223:*.webp=0;38;2;255;180;223:*.woff=0;38;2;255;180;223:*.xbps=4;38;2;154;237;254:*.xlsx=0;38;2;255;92;87:*.yaml=0;38;2;243;249;157:*.cabal=0;38;2;90;247;142:*.cache=0;38;2;102;102;102:*.class=0;38;2;102;102;102:*.cmake=0;38;2;165;255;195:*.dyn_o=0;38;2;102;102;102:*.ipynb=0;38;2;90;247;142:*.mdown=0;38;2;243;249;157:*.patch=0;38;2;90;247;142:*.scala=0;38;2;90;247;142:*.shtml=0;38;2;243;249;157:*.swift=0;38;2;90;247;142:*.toast=4;38;2;154;237;254:*.xhtml=0;38;2;243;249;157:*README=0;38;2;40;42;54;48;2;243;249;157:*passwd=0;38;2;243;249;157:*shadow=0;38;2;243;249;157:*.config=0;38;2;243;249;157:*.dyn_hi=0;38;2;102;102;102:*.flake8=0;38;2;165;255;195:*.gradle=0;38;2;90;247;142:*.groovy=0;38;2;90;247;142:*.ignore=0;38;2;165;255;195:*.matlab=0;38;2;90;247;142:*COPYING=0;38;2;153;153;153:*INSTALL=0;38;2;40;42;54;48;2;243;249;157:*LICENSE=0;38;2;153;153;153:*TODO.md=1:*.desktop=0;38;2;243;249;157:*.gemspec=0;38;2;165;255;195:*Doxyfile=0;38;2;165;255;195:*Makefile=0;38;2;165;255;195:*TODO.txt=1:*setup.py=0;38;2;165;255;195:*.DS_Store=0;38;2;102;102;102:*.cmake.in=0;38;2;165;255;195:*.fdignore=0;38;2;165;255;195:*.kdevelop=0;38;2;165;255;195:*.markdown=0;38;2;243;249;157:*.rgignore=0;38;2;165;255;195:*COPYRIGHT=0;38;2;153;153;153:*README.md=0;38;2;40;42;54;48;2;243;249;157:*configure=0;38;2;165;255;195:*.gitconfig=0;38;2;165;255;195:*.gitignore=0;38;2;165;255;195:*.localized=0;38;2;102;102;102:*.scons_opt=0;38;2;102;102;102:*CODEOWNERS=0;38;2;165;255;195:*Dockerfile=0;38;2;243;249;157:*INSTALL.md=0;38;2;40;42;54;48;2;243;249;157:*README.txt=0;38;2;40;42;54;48;2;243;249;157:*SConscript=0;38;2;165;255;195:*SConstruct=0;38;2;165;255;195:*.gitmodules=0;38;2;165;255;195:*.synctex.gz=0;38;2;102;102;102:*.travis.yml=0;38;2;90;247;142:*INSTALL.txt=0;38;2;40;42;54;48;2;243;249;157:*LICENSE-MIT=0;38;2;153;153;153:*MANIFEST.in=0;38;2;165;255;195:*Makefile.am=0;38;2;165;255;195:*Makefile.in=0;38;2;102;102;102:*.applescript=0;38;2;90;247;142:*.fdb_latexmk=0;38;2;102;102;102:*CONTRIBUTORS=0;38;2;40;42;54;48;2;243;249;157:*appveyor.yml=0;38;2;90;247;142:*configure.ac=0;38;2;165;255;195:*.clang-format=0;38;2;165;255;195:*.gitattributes=0;38;2;165;255;195:*.gitlab-ci.yml=0;38;2;90;247;142:*CMakeCache.txt=0;38;2;102;102;102:*CMakeLists.txt=0;38;2;165;255;195:*LICENSE-APACHE=0;38;2;153;153;153:*CONTRIBUTORS.md=0;38;2;40;42;54;48;2;243;249;157:*.sconsign.dblite=0;38;2;102;102;102:*CONTRIBUTORS.txt=0;38;2;40;42;54;48;2;243;249;157:*requirements.txt=0;38;2;165;255;195:*package-lock.json=0;38;2;102;102;102:*.CFUserTextEncoding=0;38;2;102;102;102"
export LS_COLORS
# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi
export EDITOR=vim

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

alias python=python3
alias pip=pip3

source ~/.iterm2_shell_integration.zsh

bindkey "^U" kill-region

if [[ -d /workspace/venv/pytorch2 ]]
then
    source /workspace/venv/pytorch2/bin/activate
fi

export PATH=/usr/local/cuda/bin:"$PATH"

cd /workspace
