#!/usr/local/bin/python3.8
#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	INTERACTIVE BROKERS FLEX WEB SERVICE
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-10-19
#* PURPOSE	DOWNLOAD IBKR FLEX WEB REPORTS
#* FILE		FLEXWEB.PY
#**********************************************************
#* MODIFICATIONS
#* 2020-10-29 - LHAYNIE - INITIAL VERSION
#**********************************************************
#ETL Stock Market Data
#Copyright 2020 Haynie IPHC, LLC
#Developed by Haynie Research & Development, LLC
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.#
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
import sys
import os
import traceback
import urllib3
import xmltodict
import yaml
import requests

settings_file = "settings.yaml"
if not os.path.exists(settings_file):
    print("settings.yaml not found!")
    sys.exit()

with open(settings_file, "r") as f:
    settings_data = yaml.load(f, Loader=yaml.FullLoader)

ibkr_token = settings_data['ibkr']['token']

if len(sys.argv) == 1:
    args = sys.argv
    print("No option provided, use --help for options.")
    exit(0)
elif len(sys.argv) == 2:
    args = sys.argv
    arg1 = sys.argv[1]
elif len(sys.argv) == 3:
    args = sys.argv
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
elif len(sys.argv) == 4:
    args = sys.argv
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
else:
    print("No option provided, use --help for options.")
    exit(0)

def get_reference(qid):
    url = f"https://gdcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.SendRequest?t={ibkr_token}&q={qid}&v=3"

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
        if data['FlexStatementResponse']['Status'] == "Success":
            response_code = data['FlexStatementResponse']['ReferenceCode']
        else:
            print("Error with IBKR response!")
            exit(1)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return response_code

def download_rpt(rcode,file):
    req = requests.get(f"https://gdcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.GetStatement?q={rcode}&t={ibkr_token}&v=3")
    url_content = req.content
    csv_file = open(file, 'wb')

    csv_file.write(url_content)
    csv_file.close()

if len(args) > 1:
    if arg1.lower() == "--help":
        print("help stuff")

    elif arg1.lower() == "--query":
        download_rpt(get_reference(arg2.lower()),arg3.lower())

    elif arg1.lower() == "--check_config":
        print("Just making sure everything works!")

    else:
        print("Error: invalid option, use --help for options.")
else:
    print("No option provided, use --help for options.")

exit(0)
