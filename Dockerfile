FROM python:3.5.4
ENV TZ="Asia/Shanghai"
RUN pip install requests python-dateutil tornado lepl && \
    mkdir app
COPY ./* ./app/
WORKDIR /app/
EXPOSE 8080
ENTRYPOINT [ "python", "./web_server.py" ]

