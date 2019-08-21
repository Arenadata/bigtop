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

baje_dir="${prefix}/usr/lib/baje"
etc_dir="${prefix}/etc/baje"
echo ${baje_dir}

install -d -m 0755 "${baje_dir}"
install -d -m 0755 "${etc_dir}"
install -d -m 0755 "${prefix}/usr/lib/systemd/system"
install -d -m 0755  "${prefix}/var/log/baje"

ls
pwd

#tar xf "nifi-assembly/target/nifi-${version}-bin.tar.gz" -C "${prefix}/usr/lib/"
cp "target/baje-${version}.jar" "${baje_dir}/baje.jar"
cp "src/main/resources/application.conf" "${etc_dir}/"
cp "src/main/resources/baje.service" "${prefix}/usr/lib/systemd/system/"
