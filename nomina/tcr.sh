#!/bin/bash
green=`tput setaf 2`
red=`tput setaf 1`
reset=`tput sgr0`

pytest .
RESULT=$?
if [ $RESULT -ne 0 ];
then
  echo "==================="
  echo  "${red}Oh no! Revert 😩${reset}"
  git checkout .

else
  echo "==================="
  echo  "${green}🙌 Let's commit! 😎${reset}"
  git add .
  git commit -m "Wip"
fi
