# kafka-elk-input

#### This is a small project to integrate and display the usage of ELK stack receiving input from a kafka-topic.

#### Usage:

  1. Install docker

  2. Install docker-compose:

    `sudo pip install docker-compose`

  3. Change the ip-address in the `docker-compose.yml` file in sub-section `KAFKA_ADVERTISED_HOST_NAME` to ip-address of your machine, remember that `localhost` DOES NOT work for some reason.

    Can also work with something like this:

    `docker run --rm debian:latest ip route | awk '/^default via / { print $3 }'`

  4. Create/Build the images using docker-compose:

    `docker-compose up`

  5. In another terminal run `producer.py` to generate data on the topic named `logstash`:

    `python producer.py`

  6. Navigate to `http://localhost:5601` to see the kibana interface and click on `Discover` tab. The data from the topic would be there.
