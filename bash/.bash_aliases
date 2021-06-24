export PATH=~/.local/bin:~/.bin:/usr/local/bin:$PATH


# bash
alias ll='ls -lh'
alias la='ls -A'
alias lal='ls -alF'
alias l.='ls -d .*'
alias l='ls -CF'
alias grep="grep --color=auto"

alias cd..='cd ..'
alias ..='cd ..'
alias ..2='cd ../..'
alias ..3='cd ../../..'
alias ..4='cd ../../../'
alias ..5='cd ../../../..'

alias www='python3 -m http.server'
alias mkcd='foo() { mkdir -p "$1"; cd "$1" }; foo '

# show open ports
alias ports='netstat -tulanp'

# aliases for applications/programs
alias vi=vim
alias ra=ranger
alias ifconfig=/sbin/ifconfig
alias ipen0='ipconfig getifaddr en0'
alias ipdig='dig +short myip.opendns.com @resolver1.opendns.com'
alias ipif='curl ifconfig.me'
alias toplinux='wget -qO - 7z.cx/o | sh'

alias lg=lazygit
alias sf="screenfetch"
alias nf="neofetch"
alias stopsk="pkill -f screenkey"
alias chwp="~/.dwm/chwp.sh"
alias tq='curl wttr.in/Beijing'
alias tqtz='curl wttr.in/Tongzhou'

if [ `uname` = 'Darwin' ]; then
    echo "Darwin"
fi
if [ `uname` = 'Linux' ]; then
    # echo "Linux"
    alias ls='ls --color=auto' #Linux only
    alias open=xdg-open # Linux only
    alias pbcopy='xsel --clipboard --input'
    alias pbpaste='xsel --clipboard --output'
fi

# commands
# rsync
# axel      - download tool
# ncdu      - disk usage analyzer with an ncurses interface
# icdiff    - improved colored diff
# cheat     - create and view interactive cheatsheets on the command-line
# dframe    - deviceframe: put device frames around your web app screenshot
# wtf       - translates acronyms and filename suffixes, e.g. wtf LOL
# tig       - text-mode interface for git
# stow      - dot file management
# zathura   - Linux pdf reader with vim style key binding 

# RVM
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*
#export PATH="$M2:$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting


# NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
#[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion
