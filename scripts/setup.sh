#!/bin/bash

echo "Enter new password"
sudo passwd ubuntu

echo "Enter Telegram Bot Username:"
read TELEGRAM_BOT_USERNAME
echo "export TELEGRAM_BOT_USERNAME=\"$TELEGRAM_BOT_USERNAME\""| sudo tee -a /etc/profile.d/env_variables.sh

echo "Enter Telegram Development Bot Username:"
read TELEGRAM_BOT_DEV_USERNAME
echo "export TELEGRAM_BOT_DEV_USERNAME=\"$TELEGRAM_BOT_DEV_USERNAME\""| sudo tee -a /etc/profile.d/env_variables.sh

echo "Enter Telegram Bot Token:"
read KIH_API_TELEGRAM_BOT_TOKEN
echo "export KIH_API_TELEGRAM_BOT_TOKEN=$KIH_API_TELEGRAM_BOT_TOKEN"| sudo tee -a /etc/profile.d/env_variables.sh

sudo timedatectl set-timezone America/New_York

sudo apt-get -y update
#sudo apt-get -y upgrade
sudo apt-get install -y lxde
sudo apt-get install -y xrdp
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
sudo apt-get install -y git-all

mkdir python_projects
git clone https://github.com/Kontinuum-Investment-Holdings/IBKR.git python_projects/IBKR
git clone https://github.com/Kontinuum-Investment-Holdings/KIH_API.git python_projects/KIH_API
mkdir python_projects/IBKR/logs && mkdir python_projects/KIH_API/logs
echo "export PYTHONPATH=\"$PYTHONPATH:$HOME/python_projects/KIH_API\""| sudo tee -a /etc/profile.d/env_variables.sh

pip install -r $HOME/python_projects/IBKR/requirements.txt
pip install -r $HOME/python_projects/KIH_API/requirements.txt

wget https://download2.interactivebrokers.com/installers/tws/latest/tws-latest-linux-x64.sh
chmod +x tws-latest-linux-x64.sh
./tws-latest-linux-x64.sh

echo "" > empty_file.txt && crontab empty_file.txt && rm -rf empty_file.txt
mkdir $HOME/logs
mkdir $HOME/logs/upgrade
crontab -l | { cat; echo "0 21 * * SAT sudo apt-get update && sudo apt-get upgrade >> $HOME/logs/upgrade/\`date +\%Y-\%m-\%d_\%H-\%M-\%S\`.log 2>&1"; } | crontab -
mkdir $HOME/logs/buy_leveraged_stocks
crontab -l | { cat; echo "0 15 * * MON-FRI cd $HOME/python_projects/IBKR && python3 jobs/buy_leveraged_stocks.py >> $HOME/logs/buy_leveraged_stocks/\`date +\%Y-\%m-\%d_\%H-\%M-\%S\`.log 2>&1"; } | crontab -

rm -rf tws-latest-linux-x64.sh
rm -rf setup.sh