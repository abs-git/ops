FROM rabbitmq:3-management

RUN mkdir -p "/var/lib/rabbitmq"
RUN chmod 666 /var/lib/rabbitmq

VOLUME ["/var/lib/rabbitmq"]

RUN rabbitmq-plugins enable --offline rabbitmq_management

EXPOSE 5672 15672

ENV RABBITMQ_CONFIG_FILE=/etc/rabbitmq/rabbitmq.conf

CMD ["rabbitmq-server"]


