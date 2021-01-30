FROM python:3
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000/tcp
EXPOSE 8000/udp

ENTRYPOINT [ "./start-server.sh"]

