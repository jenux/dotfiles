# dotfiles

Use [GNU Stow](https://www.gnu.org/software/stow/) to manage my dotfiles
Unix系统下，软件配置一般保存在$HOME下，这些文件特点是以.(dot)开头的，统称为dotfiles

为了方便维护并使用相同的配置，之前是创建一个git项目存放所有dotfiles，在不同设备上使用软链ln到正确的位置，
这种方式比较粗糙，不同的软件配置文件不止一个，配置文件的组织结构也不尽相同，手工软链容易出错

## GNU Stow

```shell
stow git
```

## 其他配置

### vimplus

``` shell
# https://github.com/chxuan/vimplus
$ git clone https://github.com/chxuan/vimplus.git ~/.vimplus
$ cd ~/.vimplus && ./update.sh
```

### Oh-My-Zsh

``` shell
# https://github.com/ohmyzsh/ohmyzsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Oh My Tmux

``` shell
# https://github.com/gpakosz/.tmux
$ cd
$ git clone https://github.com/gpakosz/.tmux.git
$ ln -s -f .tmux/.tmux.conf
$ cp .tmux/.tmux.conf.local .
```
