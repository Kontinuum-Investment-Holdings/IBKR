#!/bin/bash

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
sudo apt-get -y upgrade
sudo apt install -y ubuntu-desktop
sudo apt install -y tightvncserver
sudo apt install -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
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

vncserver :1

printf '#!/bin/sh
export XKL_XMODMAP_DISABLE=1
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey

vncconfig -iconic &
gnome-panel &
gnome-settings-daemon &
metacity &
nautilus &
gnome-terminal &'| sudo tee ~/.vnc/xstartup

vncserver -kill :1
vncserver :1

wget https://download2.interactivebrokers.com/installers/tws/latest/tws-latest-linux-x64.sh
chmod +x tws-latest-linux-x64.sh
./tws-latest-linux-x64.sh

rm -rf setup.sh