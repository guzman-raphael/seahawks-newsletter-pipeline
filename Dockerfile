FROM datajoint/pydev:python3.6

RUN apt update && apt -y install mysql-client-5.7 netcat

ENV TEAM="Seahawks"

#RUN apt update && apt -y install mysql-client-5.7 netcat

RUN mkdir /seahawks

WORKDIR /seahawks

RUN git clone https://github.com/davidgodinez/seahawks-newsletter-pipeline.git /seahawks

RUN pip install --upgrade pip && pip install . 

RUN pip insall -r requirements.txt

COPY ./dj_local_conf.json /seahawks/dj_local_conf.json

ENTRYPOINT ["bash", "-c"]

CMD ["tail -f /dev/null"] 

