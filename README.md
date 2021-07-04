# dotfiles
Use [GNU Stow](https://www.gnu.org/software/stow/) to manage my dotfiles

## vimplus
``` shell
# https://github.com/chxuan/vimplus
$ git clone https://github.com/chxuan/vimplus.git ~/.vimplus
$ cd ~/.vimplus && ./update.sh
```

## Oh-My-Zsh
``` shell
# https://github.com/ohmyzsh/ohmyzsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## Oh My Tmux
``` shell
# https://github.com/gpakosz/.tmux
$ cd
$ git clone https://github.com/gpakosz/.tmux.git
$ ln -s -f .tmux/.tmux.conf
$ cp .tmux/.tmux.conf.local .
```
