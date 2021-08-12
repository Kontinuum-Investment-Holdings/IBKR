#!/bin/bash

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
##	Installing Git
sudo apt-get install -y git-all

##	Installing Java
sudo apt install -y default-jre

##	Installing Python and it's dependencies
sudo apt-get install -y python3
sudo apt install -y python3-pip
#pip install virtualenv
echo "export PATH="$HOME/.local/bin:$PATH"" >> ~/.bash_profile && source ~/.bash_profile

## Installing other repositories required by IBeam
sudo apt-get -y install dbus-x11 xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable
sudo apt-get -y install xorg xvfb gtk2-engines-pixbuf
sudo rm -rf /var/lib/apt/lists/*

echo "******************************************************************"
echo "Initializing the Python Projects"
echo "******************************************************************"
#	Initializing Git
git config --global user.name "IBKR Service"
mkdir python_projects && cd python_projects
git clone https://github.com/Voyz/ibeam.git
git clone https://github.com/Kontinuum-Investment-Holdings/IBKR.git
git clone https://github.com/Kontinuum-Investment-Holdings/KIH_API.git


echo "******************************************************************"
echo "Setting up IBKR"
echo "******************************************************************"
##	Setting up IBKR
cd $HOME/python_projects/IBKR
mkdir logs
#virtualenv IBKR_venv
#source IBKR_venv/bin/activate
pip install -r requirements.txt --no-cache-dir

cd $HOME/python_projects/KIH_API
pip install -r requirements.txt --no-cache-dir
#deactivate
echo "export PYTHONPATH=\"$PYTHONPATH:$HOME/python_projects/KIH_API\"" >> ~/.bash_profile && source ~/.bash_profile

echo "******************************************************************"
echo "Setting up IBEAM"
echo "******************************************************************"
###	Setting up the code base
cd $HOME/python_projects/ibeam
mkdir outputs && mkdir logs
#virtualenv ibeam_venv
#source ibeam_venv/bin/activate
pip install -r requirements.txt --no-cache-dir
#deactivate
echo "export IBEAM_GATEWAY_DIR="$(pwd)/copy_cache/clientportal.gw"" >> ~/.bash_profile && source ~/.bash_profile

echo "******************************************************************"
echo "Installing Google Chrome"
echo "******************************************************************"
###	Installing Google Chrome
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
###	Installing Chome Driver
cd copy_cache
mkdir chrome_driver && cd chrome_driver
wget https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip
sudo apt-get -y update
sudo apt-get install -y unzip
unzip chromedriver_linux64.zip
rm -rf chromedriver_linux64.zip
echo "export IBEAM_CHROME_DRIVER_DIR=\"$(pwd)\"" >> ~/.bash_profile && source ~/.bash_profile
echo "export IBEAM_CHROME_DRIVER_PATH=\"$(pwd)/chromedriver\"" >> ~/.bash_profile && source ~/.bash_profile
cd ../../

echo "******************************************************************"
echo "Setting up the environmental variables"
echo "******************************************************************"
### Setting the environmental variables
echo "export IBEAM_ACCOUNT=\"kavi3515\"" >> ~/.bash_profile && source ~/.bash_profile
echo "export IBEAM_PASSWORD=\"K@v1n|)()#Inte.Pape.10\"" >> ~/.bash_profile && source ~/.bash_profile
echo "export TELEGRAM_BOT_USERNAME=\"kih_updates\"" >> ~/.bash_profile && source ~/.bash_profile
echo "export TELEGRAM_BOT_DEV_USERNAME=\"kih_updates_development\"" >> ~/.bash_profile && source ~/.bash_profile
echo "export KIH_API_TELEGRAM_BOT_TOKEN=1158382808:AAFY0iJL0LRj6TvfNmuDswIvtHNv1QOWNtU" >> ~/.bash_profile && source ~/.bash_profile

echo "******************************************************************"
echo "Starting IBeam"
echo "******************************************************************"
#	Starting IBeam
cd $HOME/python_projects/ibeam
#source ibeam_venv/bin/activate && python3 ibeam/ibeam_starter.py >> logs/ibeam.log 2>&1
#source ibeam_venv/bin/activate && nohup python3 ibeam/ibeam_starter.py -m >> logs/ibeam.log 2>&1 &
python3 ibeam/ibeam_starter.py >> logs/ibeam.log 2>&1
nohup python3 ibeam/ibeam_starter.py -m >> logs/ibeam.log 2>&1 &

echo "******************************************************************"
echo "Starting IBKR"
echo "******************************************************************"
cd $HOME/python_projects/IBKR
#source IBKR_venv/bin/activate && nohup python3 scheduler.py -m >> logs/ibkr.log 2>&1 &
nohup python3 scheduler.py -m >> logs/ibkr.log 2>&1 &

echo "******************************************************************"
echo "Deleting the script"
echo "******************************************************************"
cd $HOME
rm -rf setup.sh

echo "******************************************************************"
echo "Setup completed"
echo "******************************************************************"