# IBKR Flex Web Download [![Build Status](https://travis-ci.com/haynieresearch/ibkr_flexweb.svg?branch=master)](https://travis-ci.com/haynieresearch/ibkr_flexweb)
This program is designed to extract [Interactive Brokers](https://www.interactivebrokers.com/)) Flex Queries as local csv files.

## REQUIREMENTS
* Interactive Brokers Brokerage Account

This project is still in the early development phase and we will update this document accordingly as required.

## INSTALL
pip3 install -r requirements.txt\
rename example.settings.yaml to settings.yaml and update with your credentials\

## SETTINGS
Currently, the only setting is your [IBKR Flex Web Token](https://www.interactivebrokers.com/en/software/am/am/reports/flex_web_service_version_3.htm).

## USAGE
flexweb.py --query IBKR_QUERY_ID /path/of/your/choice/report.csv\

## GOAL
The goal of this project is simply to enable automatic download of custom reports from IBKR into our SAS environment which will be converted to SAS datasets.

## LICENSE
Copyright (c) 2020 Haynie IPHC, LLC\
Developed by Haynie Research & Development, LLC for Black Label Investment Partners, LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
