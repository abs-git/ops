FROM fluent/fluentd:v1.15-debian-1
USER root
RUN gem install fluent-plugin-elasticsearch --no-document
RUN gem install excon --no-document

USER fluent
