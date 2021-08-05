FROM voyz/ibeam

ENV PYTHONPATH "$PYTHONPATH:/home/basic_user/python/modules/pip:/home/basic_user/python/modules/KIH_API"

RUN mkdir -p /home/basic_user/scripts/
WORKDIR /home/basic_user/scripts/

RUN echo '#!/bin/bash \n\
mkdir -p $HOME/python/modules \n\
cd $HOME/python/modules \n\
rm -r KIH_API \n\
wget https://github.com/Kontinuum-Investment-Holdings/KIH_API/archive/main.tar.gz \n\
tar -xf main.tar.gz \n\
mv KIH_API-main KIH_API\n\
rm main.tar.gz \n\
\n\
rm -r IBKR \n\
wget https://github.com/Kontinuum-Investment-Holdings/IBKR/archive/main.tar.gz \n\
tar -xf main.tar.gz \n\
mv IBKR-main IBKR \n\
rm main.tar.gz \n\
\n\
cd IBKR \n\
python -m venv IBKR_venv \n\
cd .. \n\
. IBKR/IBKR_venv/bin/activate \n\
pip install --upgrade pip \n\
pip install -r KIH_API/requirements.txt \n\
pip install -r IBKR/requirements.txt \n\
\n\
python IBKR/scheduler.py' >> run.sh

RUN chmod +x run.sh

WORKDIR /srv/ibeam
RUN sed -i '2i $HOME/scripts/run.sh | tee -a $HOME/scripts/run.log &' run.sh