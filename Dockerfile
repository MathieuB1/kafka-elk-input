FROM sebp/elk

WORKDIR ${LOGSTASH_HOME}

RUN gosu logstash bin/logstash-plugin install logstash-input-kafka

RUN cd /etc/logstash/conf.d/ \
 && rm -f 01-lumberjack-input.conf 02-beats-input.conf 10-syslog.conf 11-nginx.conf \
        30-output.conf

ADD kafka.conf /etc/logstash/conf.d/kafka.conf
