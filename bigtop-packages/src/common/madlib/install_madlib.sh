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
distdir=${prefix}/usr/local/madlib

install -d -m 0755 "${distdir}/Versions/${version}/bin"
install -d -m 0755 "${distdir}/Versions/${version}/config"
install -d -m 0755 "${distdir}/Versions/${version}/doc"
install -d -m 0755 "${distdir}/Versions/${version}/lib/python"
install -d -m 0755 "${distdir}/Versions/${version}/licenses"
install -d -m 0755 "${distdir}/Versions/${version}/madpack"
install -d -m 0755 "${distdir}/Versions/${version}/ports"

cp -R build/src/bin/madpack   "${distdir}/Versions/${version}/bin/"
cp -R build/src/config/*.yml   "${distdir}/Versions/${version}/config/"
cp -R README.md "${distdir}/Versions/${version}/doc"
cp -R RELEASE_NOTES "${distdir}/Versions/${version}/doc"
cp -R build/src/lib/python/pyxb/ "${distdir}/Versions/${version}/lib/python"
find ${distdir}/Versions/${version}/lib -type f -name *.pyo -delete
find ${distdir}/Versions/${version}/lib -type f -name *.pyc -delete
find ${distdir}/Versions/${version}/madpack -type f -name *.pyo -delete
find ${distdir}/Versions/${version}/madpack -type f -name *.pyc -delete
cp -R build/src/madpack/ "${distdir}/Versions/${version}/"
cp -R build/src/ports/greenplum/ "${distdir}/Versions/${version}/ports/"
cp -R build/src/ports/postgres/ "${distdir}/Versions/${version}/ports/"
cp -R LICENSE "${distdir}/Versions/${version}/"
cp -R NOTICE "${distdir}/Versions/${version}/"
cp -R licenses/ "${distdir}/Versions/${version}/"

ln -s /usr/local/madlib/Versions/${version} ${distdir}/Current
ln -s /usr/local/madlib/Versions/${version}/bin ${distdir}/bin
ln -s /usr/local/madlib/Versions/${version}/doc ${distdir}/doc
