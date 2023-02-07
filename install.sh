list=(git bash npm ranger vim zsh)
for i in ${list[*]}; do
  stow -t $HOME -S $i || exit -1
done