# flake8: noqa

"""
AvaTax Software Development Kit for Python.

   Copyright 2022 Avalara, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

    Avalara Shipping Verification only
    API for evaluating transactions against direct-to-consumer Beverage Alcohol shipping regulations.  This API is currently in beta.  

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    2.4.5.2
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

__version__ = "2.4.5.2"

# import ApiClient
from AvalaraTest.SDK.api_client import ApiClient

# import Configuration
from AvalaraTest.SDK.configuration import Configuration

# import exceptions
from AvalaraTest.SDK.exceptions import OpenApiException
from AvalaraTest.SDK.exceptions import ApiAttributeError
from AvalaraTest.SDK.exceptions import ApiTypeError
from AvalaraTest.SDK.exceptions import ApiValueError
from AvalaraTest.SDK.exceptions import ApiKeyError
from AvalaraTest.SDK.exceptions import ApiException
