FROM voyz/ibeam

RUN #apt-get update && apt-get install -y cron

ENV PYTHONPATH "$PYTHONPATH:/home/basic_user/python/modules/KIH_API"

RUN mkdir -p /home/basic_user/scripts/
WORKDIR /home/basic_user/scripts/

RUN echo "#!/bin/bash\n" >> update.sh
RUN echo "mkdir -p $HOME/python/modules/" >> update.sh
RUN echo "cd $HOME/python/modules" >> update.sh
RUN echo "rm -r KIH_API\n" >> update.sh
RUN echo "wget https://github.com/Kontinuum-Investment-Holdings/KIH_API/archive/main.tar.gz\n" >> update.sh
RUN echo "tar -xf main.tar.gz\n" >> update.sh
RUN echo "mv KIH_API-main KIH_API\n" >> update.sh
RUN echo "rm main.tar.gz\n" >> update.sh
RUN echo "\n" >> update.sh
RUN echo "rm -r IBKR\n" >> update.sh
RUN echo "wget https://github.com/Kontinuum-Investment-Holdings/IBKR/archive/main.tar.gz\n" >> update.sh
RUN echo "tar -xf main.tar.gz\n" >> update.sh
RUN echo "mv IBKR-main IBKR\n" >> update.sh
RUN echo "rm main.tar.gz\n" >> update.sh
RUN echo "\n" >> update.sh
RUN echo "pip install --upgrade pip" >> update.sh
RUN echo "pip install --user -r KIH_API/requirements.txt" >> update.sh
RUN echo "pip install --user -r IBKR/requirements.txt" >> update.sh

RUN chmod +x update.sh
RUN ./update.sh

WORKDIR /srv/ibeam
RUN sed -i '3i python $HOME/python/modules/IBKR/scheduler.py' run.sh