#!/bin/bash

# Set KAFKA REST Proxy  specific environment variables here.

# The java implementation to use.

export JMX_PORT=9998
export KAFKAREST_HEAP_OPTS="-Xmx256M"
export KAFKAREST_JMX_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false "
