
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
import os
import sys
import boto3

PARENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, PARENT_PATH)

from configuration.initialise_config import watchmen_vars

CSV_ACCOUNTS_PATH = watchmen_vars.AccountsCsv
if watchmen_vars.UseAWSOrganisations:
    AWS_MASTER_ACCOUNT_ROLE_ARN = watchmen_vars.MasterAccountRoleArn
else:
    AWS_MASTER_ACCOUNT_ROLE_ARN = ""

def get_assumed_creds(sts, arn):
    if arn:
        credentials = sts.assume_role(
            RoleArn=arn,
            RoleSessionName="AssumeRoleSession1"
        )["Credentials"]
        return {
            "aws_access_key_id": credentials['AccessKeyId'],
            "aws_secret_access_key": credentials['SecretAccessKey'],
            "aws_session_token": credentials['SessionToken']
        }
    else:
        return {}

def get_master_linked_aws_accounts():
    creds = get_assumed_creds(boto3.client("sts", verify=False), AWS_MASTER_ACCOUNT_ROLE_ARN)
    client = boto3.client("organizations", verify=False, **creds)
    aws_accounts = set()
    for page in client.get_paginator("list_accounts").paginate():
        for account in page['Accounts']:
            aws_accounts.add(str(account[u'Id']))
    return aws_accounts

def get_csv_accounts():
    with open(CSV_ACCOUNTS_PATH) as filer:
        lines = filer.readlines()
    return {line.split(",")[0] for line in lines}

def get_accounts():
    if watchmen_vars.UseAWSOrganisations:
        master_linked_aws_accounts = get_master_linked_aws_accounts()
    else:
        master_linked_aws_accounts = set()
    csv_accounts = get_csv_accounts()
    return list(master_linked_aws_accounts | csv_accounts)
