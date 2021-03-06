# Copyright 2017 Insurance Australia Group Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#!/bin/bash
rm -rf *.cid
rm -rf unit_tests/__pycache__
rm -rf integration_tests/__pycache__
rm -rf env/
rm -rf htmlcov/
rm -rf zip_files/
rm -rf pylint/
rm -rf watchmen.egg-info/
rm -rf watchmen_cloudformation/files/citizen-update.yml
rm -rf watchmen_cloudformation/files/es-cluster.yml
rm -rf watchmen_cloudformation/files/es-subscriptions.yml
rm -rf watchmen_cloudformation/files/reporting.yml
rm -rf watchmen_cloudformation/files/roles.yml
rm -rf watchmen_cloudformation/files/watchmen.yml
rm -rf watchmen_cloudformation/files/verification-rule.yml
rm -rf citizen_cloudformation/files/citizen-rules-cfn.yml