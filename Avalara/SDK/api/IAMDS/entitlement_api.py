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
@version    2.4.33
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
from Avalara.SDK.model.IAMDS.entitlement import Entitlement
from Avalara.SDK.model.IAMDS.entitlement_list import EntitlementList
from Avalara.SDK.model.IAMDS.version_error import VersionError
from Avalara.SDK.exceptions import ApiTypeError, ApiValueError, ApiException

class EntitlementApi(object):

    def __init__(self, api_client):
        self.__set_configuration(api_client)
    
    def __verify_api_client(self,api_client):
        if api_client is None:
            raise ApiValueError("APIClient not defined")
    
    def __set_configuration(self, api_client):
        self.__verify_api_client(api_client)
        api_client.set_sdk_version("2.4.33")
        self.api_client = api_client
		
        self.create_entitlement_endpoint = _Endpoint(
            settings={
                'response_type': (Entitlement,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/entitlements',
                'operation_id': 'create_entitlement',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'x_correlation_id',
                    'entitlement',
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
                    'entitlement':
                        (Entitlement,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'entitlement': 'body',
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
        self.delete_entitlement_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/entitlements/{entitlement-id}',
                'operation_id': 'delete_entitlement',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'entitlement_id',
                    'avalara_version',
                    'x_correlation_id',
                    'if_match',
                ],
                'required': [
                    'entitlement_id',
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
                    'entitlement_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'if_match':
                        (str,),
                },
                'attribute_map': {
                    'entitlement_id': 'entitlement-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'entitlement_id': 'path',
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
        self.get_entitlement_endpoint = _Endpoint(
            settings={
                'response_type': (Entitlement,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/entitlements/{entitlement-id}',
                'operation_id': 'get_entitlement',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'entitlement_id',
                    'avalara_version',
                    'x_correlation_id',
                    'if_none_match',
                ],
                'required': [
                    'entitlement_id',
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
                    'entitlement_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'if_none_match':
                        (str,),
                },
                'attribute_map': {
                    'entitlement_id': 'entitlement-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'if_none_match': 'If-None-Match',
                },
                'location_map': {
                    'entitlement_id': 'path',
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
        self.list_entitlements_endpoint = _Endpoint(
            settings={
                'response_type': (EntitlementList,),
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/entitlements',
                'operation_id': 'list_entitlements',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter',
                    'top',
                    'skip',
                    'order_by',
                    'count',
                    'count_only',
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
        self.patch_entitlement_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/entitlements/{entitlement-id}',
                'operation_id': 'patch_entitlement',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'entitlement_id',
                    'avalara_version',
                    'x_correlation_id',
                    'if_match',
                    'entitlement',
                ],
                'required': [
                    'entitlement_id',
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
                    'entitlement_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'if_match':
                        (str,),
                    'entitlement':
                        (Entitlement,),
                },
                'attribute_map': {
                    'entitlement_id': 'entitlement-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'entitlement_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'if_match': 'header',
                    'entitlement': 'body',
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
        self.replace_entitlement_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth'
                ],
                'endpoint_path': '/entitlements/{entitlement-id}',
                'operation_id': 'replace_entitlement',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'entitlement_id',
                    'avalara_version',
                    'x_correlation_id',
                    'if_match',
                    'entitlement',
                ],
                'required': [
                    'entitlement_id',
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
                    'entitlement_id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'if_match':
                        (str,),
                    'entitlement':
                        (Entitlement,),
                },
                'attribute_map': {
                    'entitlement_id': 'entitlement-id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'entitlement_id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'if_match': 'header',
                    'entitlement': 'body',
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

    def create_entitlement(
        self,
        **kwargs
    ):
        """Create an entitlement.  # noqa: E501

        The response contains the same object as posted and fills in the newly assigned entitlement ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_entitlement(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            entitlement (Entitlement): [optional]
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
            Entitlement
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
        return self.create_entitlement_endpoint.call_with_http_info(**kwargs)

    def delete_entitlement(
        self,
        entitlement_id,
        **kwargs
    ):
        """Delete an entitlement.  # noqa: E501

        Deletes the specified entitlement.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_entitlement(entitlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            entitlement_id (str):

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
        kwargs['entitlement_id'] = \
            entitlement_id
        return self.delete_entitlement_endpoint.call_with_http_info(**kwargs)

    def get_entitlement(
        self,
        entitlement_id,
        **kwargs
    ):
        """Get an entitlement.  # noqa: E501

        Retrieves an entitlement based on its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_entitlement(entitlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            entitlement_id (str):

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
            Entitlement
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
        kwargs['entitlement_id'] = \
            entitlement_id
        return self.get_entitlement_endpoint.call_with_http_info(**kwargs)

    def list_entitlements(
        self,
        **kwargs
    ):
        """List all entitlements.  # noqa: E501

        Retrieve a list of all entitlements the authenticated user has access to. This list is paged, returning no more than 1000 items at a time.  Filterable properties:  * displayName * system/identifier * tenant/identifier * active * features/identifier * customGrants/identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_entitlements(async_req=True)
        >>> result = thread.get()


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
        return self.list_entitlements_endpoint.call_with_http_info(**kwargs)

    def patch_entitlement(
        self,
        entitlement_id,
        **kwargs
    ):
        """Update selected fields in an entitlement.  # noqa: E501

        Updates only the fields in the body of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_entitlement(entitlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            entitlement_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            if_match (str): Only execute the operation if the ETag for the current version of the resource matches the ETag in this header.. [optional]
            entitlement (Entitlement): [optional]
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
        kwargs['entitlement_id'] = \
            entitlement_id
        return self.patch_entitlement_endpoint.call_with_http_info(**kwargs)

    def replace_entitlement(
        self,
        entitlement_id,
        **kwargs
    ):
        """Update all fields in an entitlement.  # noqa: E501

        Replaces the specified entitlement with the entitlement in the body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.replace_entitlement(entitlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            entitlement_id (str):

        Keyword Args:
            avalara_version (str): States the version of the API to use.. [optional] if omitted the server will use the default value of "1.0.0"
            x_correlation_id (str): Correlation ID to pass into the method. Returned in any response.. [optional]
            if_match (str): Only execute the operation if the ETag for the current version of the resource matches the ETag in this header.. [optional]
            entitlement (Entitlement): [optional]
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
        kwargs['entitlement_id'] = \
            entitlement_id
        return self.replace_entitlement_endpoint.call_with_http_info(**kwargs)
