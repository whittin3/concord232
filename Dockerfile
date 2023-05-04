ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3

RUN \
  apk add --no-cache \
    py3-pip

# Install add-on
ADD concord232 /concord232
RUN pip3 install concord232

# Add start script
ADD start.sh /start.sh
RUN chmod a+x /start.sh

# Expose concord232 port
EXPOSE 5007

# Entrypoint
CMD /start.sh