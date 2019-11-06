#!/bin/bash

# Set Kafka KSQL specific environment variables here.

export KSQL_HEAP_OPTS="-Xmx3g"
export KSQL_JVM_PERFORMANCE_OPT="-server -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -XX:+CMSScavengeBeforeRemark -XX:+ExplicitGCInvokesConcurrent -XX:NewRatio=1 -Djava.awt.headless=true"
