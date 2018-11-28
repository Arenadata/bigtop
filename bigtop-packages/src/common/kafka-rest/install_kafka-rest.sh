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


install -d -m 0755 "${prefix}/usr/lib/kafka-rest/"
install -d -m 0755 "${prefix}/usr/lib/kafka-rest/libs/"
install -d -m 0755 "${prefix}/usr/share/"
install -d -m 0755 "${prefix}/etc/systemd/system/"



cp -R kafka-rest/target/kafka-rest-${version}-package/share/java/kafka-rest/*  "${prefix}/usr/lib/kafka-rest/libs/"
cp -R kafka-rest/target/kafka-rest-${version}-package/share/doc "${prefix}/usr/share/"
cp -R kafka-rest/target/kafka-rest-${version}-package/bin "${prefix}/usr/lib/kafka-rest/"
rm "${prefix}/usr/lib/kafka-rest/bin/kafka-rest-stop-service"
cp -R kafka-rest/target/kafka-rest-${version}-package/etc "${prefix}/"
ln -nsf "/etc/kafka-rest" "${prefix}/usr/lib/kafka-rest/config"
