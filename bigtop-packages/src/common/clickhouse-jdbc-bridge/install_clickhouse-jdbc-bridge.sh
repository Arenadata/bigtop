#!/bin/bash

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -e
set -x

prefix=$1
version=$2

install -d -m 0755 ${prefix}/usr/share/clickhouse-jdbc-bridge
install -d -m 0755 ${prefix}/var/cache/clickhouse-jdbc-bridge
install -d -m 0755 ${prefix}/var/lib/clickhouse-jdbc-bridge
install -d -m 0755 ${prefix}/var/log/clickhouse-jdbc-bridge
install -d -m 0755 ${prefix}/etc/clickhouse-jdbc-bridge
install -d -m 0755 ${prefix}/var/run/clickhouse-jdbc-bridge
install -d -m 0755 ${prefix}/etc/init.d

cp target/clickhouse-jdbc-bridge-${version}.jar ${prefix}/usr/share/clickhouse-jdbc-bridge/clickhouse-jdbc-bridge-${version}.jar
cp src/debian/etc/* ${prefix}/etc/clickhouse-jdbc-bridge/ 
#cp src/debian/init.d/clickhouse-jdbc-bridge ${prefix}/etc/init.d/clickhouse-jdbc-bridge
cp $RPM_SOURCE_DIR/clickhouse-jdbc-bridge ${prefix}/etc/init.d/clickhouse-jdbc-bridge
#cp AUTHORS CHANGELOG README.md ${prefix}/usr/share/doc/clickhouse-jdbc
#cp LICENSE ${prefix}/usr/share/licenses/clickhouse-jdbc

cd ${prefix}/usr/share/clickhouse-jdbc-bridge/
ln -s clickhouse-jdbc-bridge-${version}.jar clickhouse-jdbc-bridge.jar
