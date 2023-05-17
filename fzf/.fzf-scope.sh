#!/bin/bash

case "$1" in
  *.png) imgcat "$1" ;;
  *.svg) imgcat "$1" ;;
  *.gif) imgcat "$1" ;;
  *.jpg) imgcat "$1" ;;
  *.jpeg) imgcat "$1" ;;
  *.pdf) pdftotext "$1" ;;
  *.md) glow -s dark "$1" ;;
  *.zip) zipinfo "$1" ;;
  *.7z) 7z l "$1" ;;
  *) bat --color=always --italic-text=always --style=numbers,changes,header --line-range :500 "$1" ;;
esac
