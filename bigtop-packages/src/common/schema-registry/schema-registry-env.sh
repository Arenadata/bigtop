#!/bin/bash

# Set SCHEMA REGISTRY specific environment variables here.

# The java implementation to use.

export PID_DIR=/var/run/schema-registry
export LOG_DIR=/var/log/schema-registry
export JMX_PORT=9997
export SCHEMA_REGISTRY_HEAP_OPTS="-Xmx512M"
export SCHEMA_REGISTRY_JVM_PERFORMANCE_OPTS="-server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -Djava.awt.headless=true"