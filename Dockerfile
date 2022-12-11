FROM python:3.11.0-alpine3.15
ADD concord232 /concord232
RUN pip3 install concord232
EXPOSE 5007
CMD concord232_server --serial /dev/ttyUSB0