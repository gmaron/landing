FROM python:3.7-alpine3.9

WORKDIR /usr/app/src

ADD requirements.txt /usr/app/src

# Install required programs.
RUN pip install -r requirements.txt

COPY server/ /usr/app/src

COPY run.sh /usr/app/src/run.sh
RUN chmod +x /usr/app/src/run.sh

EXPOSE 8000

CMD ["sh", "/usr/app/src/run.sh"]
