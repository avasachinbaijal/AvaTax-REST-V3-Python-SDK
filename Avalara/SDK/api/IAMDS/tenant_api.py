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

    foundation
    Platform foundation consists of services on top of which the Avalara Compliance Cloud platform is built. These services are foundational and provide functionality such as common organization, tenant and user management for the rest of the compliance platform. 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    2.4.34
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

import re  # noqa: F401
import sys  # noqa: F401

from Avalara.SDK.api_client import ApiClient, Endpoint as _Endpoint
from Avalara.SDK.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from Avalara.SDK.model.IAMDS.device_list import DeviceList
from Avalara.SDK.model.IAMDS.entitlement_list import EntitlementList
from Avalara.SDK.model.IAMDS.grant_list import GrantList
from Avalara.SDK.model.IAMDS.group_list import GroupList
from Avalara.SDK.model.IAMDS.tenant import Tenant
from Avalara.SDK.model.IAMDS.tenant_list import TenantList
from Avalara.SDK.model.IAMDS.user_list import UserList
from Avalara.SDK.model.IAMDS.version_error import VersionError
from Avalara.SDK.exceptions import ApiTypeError, ApiValueError, ApiException

class TenantApi(object):

    def __init__(self, api_client):
        self.__set_configuration(api_client)
    
    def __verify_api_client(self,api_client):
        if api_client is None:
            raise ApiValueError("APIClient not defined")
    
    def __set_configuration(self, api_client):
        self.__verify_api_client(api_client)
        api_client.set_sdk_version("2.4.34")
        self.api_client = api_client
		
        self.add_device_to_tenant_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/devices/{device-id}',
                'operation_id': 'add_device_to_tenant',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'device_id',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'device_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'device_id': 'device-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'device_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.add_grant_to_tenant_user_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/users/{user-id}/grants/{grant-id}',
                'operation_id': 'add_grant_to_tenant_user',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'user_id',
                    'grant_id',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                    'user_id',
                    'grant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'user_id':
                        (str,),
                    'grant_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'user_id': 'user-id',
                    'grant_id': 'grant-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'user_id': 'path',
                    'grant_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.add_user_to_tenant_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/users/{user-id}',
                'operation_id': 'add_user_to_tenant',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'user_id',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'user_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'user_id': 'user-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'user_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.create_tenant_endpoint = _Endpoint(
            settings={
                'response_type': (Tenant,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants',
                'operation_id': 'create_tenant',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'x_correlation_id',
                    'tenant',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'tenant':
                        (Tenant,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'tenant': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_tenant_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}',
                'operation_id': 'delete_tenant',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'avalara_version',
                    'x_correlation_id',
                    'if_match',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'if_match':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'if_match': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_tenant_endpoint = _Endpoint(
            settings={
                'response_type': (Tenant,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}',
                'operation_id': 'get_tenant',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'avalara_version',
                    'x_correlation_id',
                    'if_none_match',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'if_none_match':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'if_none_match': 'If-None-Match',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'if_none_match': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tenant_devices_endpoint = _Endpoint(
            settings={
                'response_type': (DeviceList,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/devices',
                'operation_id': 'list_tenant_devices',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'filter',
                    'top',
                    'skip',
                    'order_by',
                    'count',
                    'count_only',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'filter':
                        (str,),
                    'top':
                        (str,),
                    'skip':
                        (str,),
                    'order_by':
                        (str,),
                    'count':
                        (bool,),
                    'count_only':
                        (bool,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'order_by': '$orderBy',
                    'count': 'count',
                    'count_only': 'countOnly',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'order_by': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tenant_entitlements_endpoint = _Endpoint(
            settings={
                'response_type': (EntitlementList,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/entitlements',
                'operation_id': 'list_tenant_entitlements',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'filter',
                    'top',
                    'skip',
                    'order_by',
                    'count',
                    'count_only',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'filter':
                        (str,),
                    'top':
                        (str,),
                    'skip':
                        (str,),
                    'order_by':
                        (str,),
                    'count':
                        (bool,),
                    'count_only':
                        (bool,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'order_by': '$orderBy',
                    'count': 'count',
                    'count_only': 'countOnly',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'order_by': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tenant_groups_endpoint = _Endpoint(
            settings={
                'response_type': (GroupList,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/groups',
                'operation_id': 'list_tenant_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'filter',
                    'top',
                    'skip',
                    'order_by',
                    'count',
                    'count_only',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'filter':
                        (str,),
                    'top':
                        (str,),
                    'skip':
                        (str,),
                    'order_by':
                        (str,),
                    'count':
                        (bool,),
                    'count_only':
                        (bool,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'order_by': '$orderBy',
                    'count': 'count',
                    'count_only': 'countOnly',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'order_by': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tenant_user_grants_endpoint = _Endpoint(
            settings={
                'response_type': (GrantList,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/users/{user-id}/grants',
                'operation_id': 'list_tenant_user_grants',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'user_id',
                    'filter',
                    'top',
                    'skip',
                    'order_by',
                    'count',
                    'count_only',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'user_id':
                        (str,),
                    'filter':
                        (str,),
                    'top':
                        (str,),
                    'skip':
                        (str,),
                    'order_by':
                        (str,),
                    'count':
                        (bool,),
                    'count_only':
                        (bool,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'user_id': 'user-id',
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'order_by': '$orderBy',
                    'count': 'count',
                    'count_only': 'countOnly',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'user_id': 'path',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'order_by': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tenant_user_groups_endpoint = _Endpoint(
            settings={
                'response_type': (GroupList,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/users/{user-id}/groups',
                'operation_id': 'list_tenant_user_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'user_id',
                    'filter',
                    'top',
                    'skip',
                    'order_by',
                    'count',
                    'count_only',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'user_id':
                        (str,),
                    'filter':
                        (str,),
                    'top':
                        (str,),
                    'skip':
                        (str,),
                    'order_by':
                        (str,),
                    'count':
                        (bool,),
                    'count_only':
                        (bool,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'user_id': 'user-id',
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'order_by': '$orderBy',
                    'count': 'count',
                    'count_only': 'countOnly',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'user_id': 'path',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'order_by': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tenant_users_endpoint = _Endpoint(
            settings={
                'response_type': (UserList,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/users',
                'operation_id': 'list_tenant_users',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'filter',
                    'top',
                    'skip',
                    'order_by',
                    'count',
                    'count_only',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'filter':
                        (str,),
                    'top':
                        (str,),
                    'skip':
                        (str,),
                    'order_by':
                        (str,),
                    'count':
                        (bool,),
                    'count_only':
                        (bool,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'order_by': '$orderBy',
                    'count': 'count',
                    'count_only': 'countOnly',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'order_by': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tenants_endpoint = _Endpoint(
            settings={
                'response_type': (TenantList,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants',
                'operation_id': 'list_tenants',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter',
                    'top',
                    'skip',
                    'count',
                    'count_only',
                    'order_by',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'filter':
                        (str,),
                    'top':
                        (str,),
                    'skip':
                        (str,),
                    'count':
                        (bool,),
                    'count_only':
                        (bool,),
                    'order_by':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'count': 'count',
                    'count_only': 'countOnly',
                    'order_by': '$orderBy',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'order_by': 'query',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.patch_tenant_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}',
                'operation_id': 'patch_tenant',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'avalara_version',
                    'x_correlation_id',
                    'if_match',
                    'tenant',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'if_match':
                        (str,),
                    'tenant':
                        (Tenant,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'if_match': 'header',
                    'tenant': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.remove_device_from_tenant_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/devices/{device-id}',
                'operation_id': 'remove_device_from_tenant',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'device_id',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'device_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'device_id': 'device-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'device_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.remove_grant_from_tenant_user_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/users/{user-id}/grants/{grant-id}',
                'operation_id': 'remove_grant_from_tenant_user',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'user_id',
                    'grant_id',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                    'user_id',
                    'grant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'user_id':
                        (str,),
                    'grant_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'user_id': 'user-id',
                    'grant_id': 'grant-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'user_id': 'path',
                    'grant_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.remove_user_from_tenant_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}/users/{user-id}',
                'operation_id': 'remove_user_from_tenant',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'user_id',
                    'avalara_version',
                    'x_correlation_id',
                ],
                'required': [
                    'tenant_id',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'user_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'user_id': 'user-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'user_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.replace_tenant_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/tenants/{tenant-id}',
                'operation_id': 'replace_tenant',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'avalara_version',
                    'x_correlation_id',
                    'if_match',
                    'tenant',
                ],
                'required': [
                    'tenant_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'avalara_version',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('avalara_version',): {

                        "1.0.0": "1.0.0"
                    },
                },
                'openapi_types': {
                    'tenant_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'if_match':
                        (str,),
                    'tenant':
                        (Tenant,),
                },
                'attribute_map': {
                    'tenant_id': 'tenant-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'tenant_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'if_match': 'header',
                    'tenant': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def add_device_to_tenant(
        self,
        tenant_id,
        device_id,
        **kwargs
    ):
        """Add a device to a tenant.  # noqa: E501

        Adds a device to a tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_device_to_tenant(tenant_id, device_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):
            device_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        kwargs['device_id'] = \
            device_id
        return self.add_device_to_tenant_endpoint.call_with_http_info(**kwargs)

    def add_grant_to_tenant_user(
        self,
        tenant_id,
        user_id,
        grant_id,
        **kwargs
    ):
        """Add a grant to a user within a tenant.  # noqa: E501

        Adds a grant to a user within a tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_grant_to_tenant_user(tenant_id, user_id, grant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):
            user_id (str):
            grant_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        kwargs['user_id'] = \
            user_id
        kwargs['grant_id'] = \
            grant_id
        return self.add_grant_to_tenant_user_endpoint.call_with_http_info(**kwargs)

    def add_user_to_tenant(
        self,
        tenant_id,
        user_id,
        **kwargs
    ):
        """Add a user to a tenant.  # noqa: E501

        Adds a user to a tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_user_to_tenant(tenant_id, user_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):
            user_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        kwargs['user_id'] = \
            user_id
        return self.add_user_to_tenant_endpoint.call_with_http_info(**kwargs)

    def create_tenant(
        self,
        **kwargs
    ):
        """Add a tenant to the list of tenants.  # noqa: E501

        On a post, the tenant ID will not be known since it is assigned by the system. The response contains the tenant, including ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_tenant(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            tenant (Tenant): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Tenant
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.create_tenant_endpoint.call_with_http_info(**kwargs)

    def delete_tenant(
        self,
        tenant_id,
        **kwargs
    ):
        """Delete a tenant.  # noqa: E501

        Deletes the specified tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_tenant(tenant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            if_match (str): Only execute the operation if the ETag for the current version of the resource matches the ETag in this header.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        return self.delete_tenant_endpoint.call_with_http_info(**kwargs)

    def get_tenant(
        self,
        tenant_id,
        **kwargs
    ):
        """GET a tenant by ID.  # noqa: E501

        Retrieves the specified tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tenant(tenant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            if_none_match (str): Only return the resource if the ETag is different from the ETag passed in.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Tenant
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        return self.get_tenant_endpoint.call_with_http_info(**kwargs)

    def list_tenant_devices(
        self,
        tenant_id,
        **kwargs
    ):
        """Retrieve all devices within a tenant.  # noqa: E501

        Retrieve a list of all devices within a tenant which the authenticated user has access to. This list is paged, returning no more than 1000 items at a time.  Filterable properties:   * displayName * grants/identifier * active * groups/identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tenant_devices(tenant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):

        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve.. [optional]
            top (str): If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional]
            skip (str): If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets.. [optional]
            order_by (str): A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.. [optional]
            count (bool): If set to 'true', requests the count of items as part of the response. Default: 'false'. If the value cannot be. [optional]
            count_only (bool): If set to 'true', requests the count of items as part of the response. No values are returned. Default: 'false'.. [optional]
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DeviceList
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        return self.list_tenant_devices_endpoint.call_with_http_info(**kwargs)

    def list_tenant_entitlements(
        self,
        tenant_id,
        **kwargs
    ):
        """Retrieve all entitlements within a tenant.  # noqa: E501

        Retrieve a list of all entitlements on the tenant. This list is paged, returning no more than 1000 items at a time.  Filterable properties:   * displayName * system/identifier * active * features/identifier * customGrants/identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tenant_entitlements(tenant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):

        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve.. [optional]
            top (str): If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional]
            skip (str): If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets.. [optional]
            order_by (str): A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.. [optional]
            count (bool): If set to 'true', requests the count of items as part of the response. Default: 'false'. If the value cannot be. [optional]
            count_only (bool): If set to 'true', requests the count of items as part of the response. No values are returned. Default: 'false'.. [optional]
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            EntitlementList
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        return self.list_tenant_entitlements_endpoint.call_with_http_info(**kwargs)

    def list_tenant_groups(
        self,
        tenant_id,
        **kwargs
    ):
        """Retrieve all groups within a tenant.  # noqa: E501

        Retrieve a list of all groups on the tenant. This list is paged, returning no more than 1000 items at a time.  Filterable properties:   * displayName * grants/identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tenant_groups(tenant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):

        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve.. [optional]
            top (str): If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional]
            skip (str): If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets.. [optional]
            order_by (str): A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.. [optional]
            count (bool): If set to 'true', requests the count of items as part of the response. Default: 'false'. If the value cannot be. [optional]
            count_only (bool): If set to 'true', requests the count of items as part of the response. No values are returned. Default: 'false'.. [optional]
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GroupList
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        return self.list_tenant_groups_endpoint.call_with_http_info(**kwargs)

    def list_tenant_user_grants(
        self,
        tenant_id,
        user_id,
        **kwargs
    ):
        """Add a grant to a user within a tenant.  # noqa: E501

        Retrieve a list of all grants a user belongs to within the tenant which the authenticated user has access to. This list is paged, returning no more than 1000 items at a time.  Filterable properties:   * displayName * grants/identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tenant_user_grants(tenant_id, user_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):
            user_id (str):

        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve.. [optional]
            top (str): If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional]
            skip (str): If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets.. [optional]
            order_by (str): A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.. [optional]
            count (bool): If set to 'true', requests the count of items as part of the response. Default: 'false'. If the value cannot be. [optional]
            count_only (bool): If set to 'true', requests the count of items as part of the response. No values are returned. Default: 'false'.. [optional]
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GrantList
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        kwargs['user_id'] = \
            user_id
        return self.list_tenant_user_grants_endpoint.call_with_http_info(**kwargs)

    def list_tenant_user_groups(
        self,
        tenant_id,
        user_id,
        **kwargs
    ):
        """List the groups a user belongs to within a specific tenant.  # noqa: E501

        Retrieve a list of all groups a user belongs to within the tenant which the authenticated user has access to. This list is paged, returning no more than 1000 items at a time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tenant_user_groups(tenant_id, user_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):
            user_id (str):

        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve.. [optional]
            top (str): If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional]
            skip (str): If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets.. [optional]
            order_by (str): A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.. [optional]
            count (bool): If set to 'true', requests the count of items as part of the response. Default: 'false'. If the value cannot be. [optional]
            count_only (bool): If set to 'true', requests the count of items as part of the response. No values are returned. Default: 'false'.. [optional]
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GroupList
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        kwargs['user_id'] = \
            user_id
        return self.list_tenant_user_groups_endpoint.call_with_http_info(**kwargs)

    def list_tenant_users(
        self,
        tenant_id,
        **kwargs
    ):
        """Retrieve all users within a tenant.  # noqa: E501

        Retrieve a list of all users within the tenant which the authenticated user has access to. This list is paged, returning no more than 1000 items at a time.  Filterable properties:   * displayName * emails/value * active * userName * grants/identifier * groups/identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tenant_users(tenant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):

        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve.. [optional]
            top (str): If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional]
            skip (str): If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets.. [optional]
            order_by (str): A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.. [optional]
            count (bool): If set to 'true', requests the count of items as part of the response. Default: 'false'. If the value cannot be. [optional]
            count_only (bool): If set to 'true', requests the count of items as part of the response. No values are returned. Default: 'false'.. [optional]
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserList
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        return self.list_tenant_users_endpoint.call_with_http_info(**kwargs)

    def list_tenants(
        self,
        **kwargs
    ):
        """Get a list of all tenants.  # noqa: E501

        Retrieve a list of all tenants the authenticated user has access to. This list is paged, returning no more than 1000 items at a time.  Filterable properties:   * displayName * organization/identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tenants(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve.. [optional]
            top (str): If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional]
            skip (str): If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets.. [optional]
            count (bool): If set to 'true', requests the count of items as part of the response. Default: 'false'. If the value cannot be. [optional]
            count_only (bool): If set to 'true', requests the count of items as part of the response. No values are returned. Default: 'false'.. [optional]
            order_by (str): A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.. [optional]
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TenantList
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_tenants_endpoint.call_with_http_info(**kwargs)

    def patch_tenant(
        self,
        tenant_id,
        **kwargs
    ):
        """Update specific fields in a tenant.  # noqa: E501

        Updates the fields on a tenant which should change.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_tenant(tenant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            if_match (str): Only execute the operation if the ETag for the current version of the resource matches the ETag in this header.. [optional]
            tenant (Tenant): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        return self.patch_tenant_endpoint.call_with_http_info(**kwargs)

    def remove_device_from_tenant(
        self,
        tenant_id,
        device_id,
        **kwargs
    ):
        """Remove a device from a tenant.  # noqa: E501

        Removes a device from a tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_device_from_tenant(tenant_id, device_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):
            device_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        kwargs['device_id'] = \
            device_id
        return self.remove_device_from_tenant_endpoint.call_with_http_info(**kwargs)

    def remove_grant_from_tenant_user(
        self,
        tenant_id,
        user_id,
        grant_id,
        **kwargs
    ):
        """Remove a grant from a user within a tenant.  # noqa: E501

        Removes a grant from a user on a tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_grant_from_tenant_user(tenant_id, user_id, grant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):
            user_id (str):
            grant_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        kwargs['user_id'] = \
            user_id
        kwargs['grant_id'] = \
            grant_id
        return self.remove_grant_from_tenant_user_endpoint.call_with_http_info(**kwargs)

    def remove_user_from_tenant(
        self,
        tenant_id,
        user_id,
        **kwargs
    ):
        """Remove a user from a tenant.  # noqa: E501

        Removes a user from a tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_user_from_tenant(tenant_id, user_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):
            user_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        kwargs['user_id'] = \
            user_id
        return self.remove_user_from_tenant_endpoint.call_with_http_info(**kwargs)

    def replace_tenant(
        self,
        tenant_id,
        **kwargs
    ):
        """Update a tenant by ID.  # noqa: E501

        Updates the tenant with the data in the request body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.replace_tenant(tenant_id, async_req=True)
        >>> result = thread.get()

        Args:
            tenant_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            if_match (str): Only execute the operation if the ETag for the current version of the resource matches the ETag in this header.. [optional]
            tenant (Tenant): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['tenant_id'] = \
            tenant_id
        return self.replace_tenant_endpoint.call_with_http_info(**kwargs)

