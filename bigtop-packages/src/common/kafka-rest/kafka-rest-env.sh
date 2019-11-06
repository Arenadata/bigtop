#!/bin/bash

# Set Kafka REST Proxy specific environment variables here.

export KAFKAREST_HEAP_OPTS="-Xmx1024M"
export KAFKAREST_JMX_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"
