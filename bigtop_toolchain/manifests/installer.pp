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

class bigtop_toolchain::installer {

  if versioncmp($::puppetversion,'3.6.1') >= 0 {
    $allow_virtual_packages = hiera('allow_virtual_packages',false)
    Package {
      allow_virtual => $allow_virtual_packages,
    }
  }

  include bigtop_toolchain::jdk
  include bigtop_toolchain::maven
  include bigtop_toolchain::ant
  include bigtop_toolchain::gradle
  include bigtop_toolchain::node
  include bigtop_toolchain::protobuf
  include bigtop_toolchain::packages
  include bigtop_toolchain::env
  include bigtop_toolchain::user
  include bigtop_toolchain::renv

  stage { 'last':
    require => Stage['main'],
  }
  class { 'bigtop_toolchain::cleanup': stage => 'last' }
}

