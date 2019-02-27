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


install -d -m 0755 "${prefix}/usr/lib/ksql/"
install -d -m 0755 "${prefix}/usr/lib/ksql/libs/"
install -d -m 0755 "${prefix}/usr/share/"
install -d -m 0755 "${prefix}/usr/lib/systemd/system/"
install -d -m 0755 "${prefix}/usr/bin/"



cp -R ksql-package/target/ksql-package-${version}-package/share/java/ksql/*  "${prefix}/usr/lib/ksql/libs/"
cp -R ksql-package/target/ksql-package-${version}-package/share/doc "${prefix}/usr/share/"

cp -R ksql-package/target/ksql-package-${version}-package/bin "${prefix}/usr/lib/ksql/"
cp -R ksql-package/target/ksql-package-${version}-package/ext "${prefix}/usr/lib/ksql/"
cp -R ksql-package/target/ksql-package-${version}-package/resources "${prefix}/usr/lib/ksql/"

cp -R ksql-package/target/ksql-package-${version}-package/etc "${prefix}/"
ln -nsf "/etc/ksql" "${prefix}/usr/lib/ksql/config"
