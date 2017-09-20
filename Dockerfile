FROM python:3.5.4
RUN pip install requests python-dateutil tornado && \
    mkdir app
COPY ./* ./app/
WORKDIR /app/
EXPOSE 8080
CMD python web_server.py
