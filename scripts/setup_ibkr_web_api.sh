#!/bin/bash

echo "******************************************************************"
echo "Getting user specific data"
echo "******************************************************************"

echo "Enter IBKR Username:"
read IBEAM_ACCOUNT

echo "Enter IBKR Password:"
read IBEAM_PASSWORD

echo "Enter Telegram Bot Username:"
read TELEGRAM_BOT_USERNAME

echo "Enter Telegram Development Bot Username:"
read TELEGRAM_BOT_DEV_USERNAME

echo "Enter Telegram Bot Token:"
read KIH_API_TELEGRAM_BOT_TOKEN

echo "******************************************************************"
echo "Initializing"
echo "******************************************************************"
cd $HOME

#	Changing the timezone to New York Standard Time
sudo timedatectl set-timezone America/New_York

# Removing old installations, if any
echo "" > ~/.bash_profile
rm -rf python_projects

#	Updating and upgrading packages
sudo apt-get -y update && sudo apt-get -y upgrade

echo "******************************************************************"
echo "Installing required software"
echo "******************************************************************"
sudo apt-get install -y git-all

sudo apt install -y default-jre

sudo apt-get install -y python3
sudo apt install -y python3-pip
echo "export PATH="$HOME/.local/bin:$PATH"" >> ~/.bash_profile && source ~/.bash_profile

## Installing other repositories required by IBeam
sudo apt-get -y install dbus-x11 xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable
sudo apt-get -y install xorg xvfb gtk2-engines-pixbuf
sudo rm -rf /var/lib/apt/lists/*

echo "******************************************************************"
echo "Initializing the Python Projects"
echo "******************************************************************"
git config --global user.name "IBKR Service"
mkdir python_projects && cd python_projects
git clone https://github.com/Voyz/ibeam.git
git clone https://github.com/Kontinuum-Investment-Holdings/IBKR.git
git clone https://github.com/Kontinuum-Investment-Holdings/KIH_API.git


echo "******************************************************************"
echo "Setting up IBKR"
echo "******************************************************************"
cd $HOME/python_projects/IBKR
mkdir logs
pip install -r requirements.txt --no-cache-dir

cd $HOME/python_projects/KIH_API
pip install -r requirements.txt --no-cache-dir
echo "export PYTHONPATH=\"$PYTHONPATH:$HOME/python_projects/KIH_API\"" >> ~/.bash_profile

echo "******************************************************************"
echo "Setting up IBEAM"
echo "******************************************************************"
cd $HOME/python_projects/ibeam
mkdir outputs && mkdir logs
pip install -r requirements.txt --no-cache-dir
echo "export IBEAM_GATEWAY_DIR="$(pwd)/copy_cache/clientportal.gw"" >> ~/.bash_profile

echo "******************************************************************"
echo "Installing Google Chrome"
echo "******************************************************************"
mkdir temp && cd temp
sudo apt-get -y install wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get -y update
sudo apt install -y $(pwd)/google-chrome-stable_current_amd64.deb
rm -rf google-chrome-stable_current_amd64.deb
cd ..
rm -r temp

echo "******************************************************************"
echo "Installing the Chrome Driver"
echo "******************************************************************"
cd copy_cache
mkdir chrome_driver && cd chrome_driver
wget https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip
sudo apt-get -y update
sudo apt-get install -y unzip
unzip chromedriver_linux64.zip
rm -rf chromedriver_linux64.zip
echo "export IBEAM_CHROME_DRIVER_DIR=\"$(pwd)\"" >> ~/.bash_profile
echo "export IBEAM_CHROME_DRIVER_PATH=\"$(pwd)/chromedriver\"" >> ~/.bash_profile
cd ../../

echo "******************************************************************"
echo "Setting up the environmental variables"
echo "******************************************************************"
echo "export IBEAM_ACCOUNT=\"$IBEAM_ACCOUNT\"" >> ~/.bash_profile
echo "export IBEAM_PASSWORD=\"$IBEAM_PASSWORD\"" >> ~/.bash_profile
echo "export TELEGRAM_BOT_USERNAME=\"$TELEGRAM_BOT_USERNAME\"" >> ~/.bash_profile
echo "export TELEGRAM_BOT_DEV_USERNAME=\"$TELEGRAM_BOT_DEV_USERNAME\"" >> ~/.bash_profile
echo "export KIH_API_TELEGRAM_BOT_TOKEN=$KIH_API_TELEGRAM_BOT_TOKEN" >> ~/.bash_profile
source ~/.bash_profile

echo "******************************************************************"
echo "Starting IBeam"
echo "******************************************************************"
cd $HOME/python_projects/ibeam
python3 ibeam/ibeam_starter.py >> logs/ibeam.log 2>&1
nohup python3 ibeam/ibeam_starter.py -m >> logs/ibeam.log 2>&1 &

echo "******************************************************************"
echo "Starting IBKR"
echo "******************************************************************"
cd $HOME/python_projects/IBKR
nohup python3 scheduler.py -m >> logs/ibkr.log 2>&1 &

echo "******************************************************************"
echo "Deleting the script"
echo "******************************************************************"
cd $HOME
rm -rf setup.sh

echo "******************************************************************"
echo "Setup completed"
echo "******************************************************************"