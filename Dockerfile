FROM voyz/ibeam

ENV PYTHONPATH "$PYTHONPATH:/home/basic_user/python/modules/KIH_API"
RUN mkdir -p /home/basic_user/python/modules/

WORKDIR /home/basic_user/python/modules/

#   Installing KIH_API
RUN wget https://github.com/Kontinuum-Investment-Holdings/KIH_API/archive/master.tar.gz
RUN tar \-xf master.tar.gz
RUN mv KIH_API-master KIH_API
RUN rm master.tar.gz

#   Installing IBKR
RUN wget https://github.com/Kontinuum-Investment-Holdings/IBKR/archive/main.tar.gz
RUN tar \-xf main.tar.gz
RUN mv IBKR-main IBKR
RUN rm main.tar.gz

WORKDIR /srv/ibeam