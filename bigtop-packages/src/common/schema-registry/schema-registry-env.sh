#!/bin/bash

# Set SCHEMA REGISTRY specific environment variables here.

export SCHEMA_REGISTRY_HEAP_OPTS="-Xmx1024M"
export SCHEMA_REGISTRY_JVM_PERFORMANCE_OPTS="-server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -Djava.awt.headless=true"
