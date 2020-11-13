#!/bin/bash
apt update -y
apt upgrade -y
apt install php unzip python python2 curl wget openssh toilet fish clang cowsay -y
unzip *.zip 
ssh-keygen -t rsa
clear
toilet -f mono9 'done'
cowsay "you can open the tool with command \npython3 start.py"
