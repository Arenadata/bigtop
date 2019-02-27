#!/bin/bash

# Set KSQL specific environment variables here.

# The java implementation to use.

export KSQL_HEAP_OPTS="-Xmx3g"
export KSQL_JVM_PERFORMANCE_OPT="-server -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -XX:+CMSScavengeBeforeRemark -XX:+ExplicitGCInvokesConcurrent -XX:NewRatio=1 -Djava.awt.headless=true"
