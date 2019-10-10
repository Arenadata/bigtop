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

minifi_dir="${prefix}/usr/lib/minifi"
minifi_c2_dir="${prefix}/usr/lib/minifi-c2"
etc_dir="${prefix}/etc/minifi"
c2_etc_dir="${prefix}/etc/minifi-c2"

install -d -m 0755 "${prefix}/usr/lib/"
install -d -m 0755 "${etc_dir}"
install -d -m 0755 "${prefix}/var/log/minifi"
install -d -m 0755 "${prefix}/usr/lib/systemd/system/"
install -d -m 0755 "${c2_etc_dir}"

tar xf "minifi-assembly/target/minifi-${version}-bin.tar.gz" -C "${prefix}/usr/lib/"
mv "${prefix}/usr/lib/minifi-${version}" "${minifi_dir}"
mv "${minifi_dir}/conf" "${etc_dir}/conf"
cp -r "${etc_dir}/conf" "${etc_dir}/conf.dist"

ln -nsf "/etc/minifi/conf" "${minifi_dir}/conf"


tar xf "minifi-c2/minifi-c2-assembly/target//minifi-c2-${version}-bin.tar.gz" -C "${prefix}/usr/lib/"
mv "${prefix}/usr/lib/minifi-c2-${version}" "${minifi_c2_dir}"
mv "${minifi_c2_dir}/conf" "${c2_etc_dir}/conf"
cp -r "${c2_etc_dir}/conf" "${c2_etc_dir}/conf.dist"

ln -nsf "/etc/minifi-c2/conf" "${minifi_c2_dir}/conf"

tar xf "minifi-toolkit/minifi-toolkit-assembly/target/minifi-toolkit-${version}-bin.tar.gz" -C "${prefix}/usr/lib/"
mv "${prefix}/usr/lib/minifi-toolkit-${version}" "${prefix}/usr/lib/minifi-toolkit"

