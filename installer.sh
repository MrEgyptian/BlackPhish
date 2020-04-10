#!/bin/bash
apt update -y
apt upgrade -y
apt install php python python2 curl wget openssh toilet fish clang cowsay -y
unzip *.zip 
clear
toilet -f mono9 'done'
cowsay "you can open the tool with command \npython3 start.py"
