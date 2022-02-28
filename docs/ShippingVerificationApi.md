# Avalara.SDK.ShippingVerificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deregister_shipment**](ShippingVerificationApi.md#deregister_shipment) | **DELETE** /api/v2/companies/{companyCode}/transactions/{transactionCode}/shipment/registration | Removes the transaction from consideration when evaluating regulations that span multiple transactions.
[**register_shipment**](ShippingVerificationApi.md#register_shipment) | **PUT** /api/v2/companies/{companyCode}/transactions/{transactionCode}/shipment/registration | Registers the transaction so that it may be included when evaluating regulations that span multiple transactions.
[**register_shipment_if_compliant**](ShippingVerificationApi.md#register_shipment_if_compliant) | **PUT** /api/v2/companies/{companyCode}/transactions/{transactionCode}/shipment/registerIfCompliant | Evaluates a transaction against a set of direct-to-consumer shipping regulations and, if compliant, registers the transaction so that it may be included when evaluating regulations that span multiple transactions.
[**verify_shipment**](ShippingVerificationApi.md#verify_shipment) | **GET** /api/v2/companies/{companyCode}/transactions/{transactionCode}/shipment/verify | Evaluates a transaction against a set of direct-to-consumer shipping regulations.


# **deregister_shipment**
> deregister_shipment(company_code, transaction_code)

Removes the transaction from consideration when evaluating regulations that span multiple transactions.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import shipping_verification_api
from Avalara.SDK.model.error_details import ErrorDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = Avalara.SDK.Configuration(
    username = 'YOUR USERNAME',
    password = 'YOUR PASSWORD',
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping_verification_api.ShippingVerificationApi(api_client)
    company_code = "companyCode_example" # str | The company code of the company that recorded the transaction
    transaction_code = "transactionCode_example" # str | The transaction code to retrieve
    document_type = "SalesInvoice" # str | (Optional): The document type of the transaction to operate on. If omitted, defaults to \"SalesInvoice\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Removes the transaction from consideration when evaluating regulations that span multiple transactions.
        api_instance.deregister_shipment(company_code, transaction_code)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ShippingVerificationApi->deregister_shipment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes the transaction from consideration when evaluating regulations that span multiple transactions.
        api_instance.deregister_shipment(company_code, transaction_code, document_type=document_type)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ShippingVerificationApi->deregister_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_code** | **str**| The company code of the company that recorded the transaction |
 **transaction_code** | **str**| The transaction code to retrieve |
 **document_type** | **str**| (Optional): The document type of the transaction to operate on. If omitted, defaults to \&quot;SalesInvoice\&quot; | [optional]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Invalid Transaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_shipment**
> register_shipment(company_code, transaction_code)

Registers the transaction so that it may be included when evaluating regulations that span multiple transactions.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import shipping_verification_api
from Avalara.SDK.model.error_details import ErrorDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = Avalara.SDK.Configuration(
    username = 'YOUR USERNAME',
    password = 'YOUR PASSWORD',
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping_verification_api.ShippingVerificationApi(api_client)
    company_code = "companyCode_example" # str | The company code of the company that recorded the transaction
    transaction_code = "transactionCode_example" # str | The transaction code to retrieve
    document_type = "SalesInvoice" # str | (Optional): The document type of the transaction to operate on. If omitted, defaults to \"SalesInvoice\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Registers the transaction so that it may be included when evaluating regulations that span multiple transactions.
        api_instance.register_shipment(company_code, transaction_code)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ShippingVerificationApi->register_shipment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Registers the transaction so that it may be included when evaluating regulations that span multiple transactions.
        api_instance.register_shipment(company_code, transaction_code, document_type=document_type)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ShippingVerificationApi->register_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_code** | **str**| The company code of the company that recorded the transaction |
 **transaction_code** | **str**| The transaction code to retrieve |
 **document_type** | **str**| (Optional): The document type of the transaction to operate on. If omitted, defaults to \&quot;SalesInvoice\&quot; | [optional]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Invalid Transaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_shipment_if_compliant**
> ShippingVerifyResult register_shipment_if_compliant(company_code, transaction_code)

Evaluates a transaction against a set of direct-to-consumer shipping regulations and, if compliant, registers the transaction so that it may be included when evaluating regulations that span multiple transactions.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import shipping_verification_api
from Avalara.SDK.model.shipping_verify_result import ShippingVerifyResult
from Avalara.SDK.model.error_details import ErrorDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = Avalara.SDK.Configuration(
    username = 'YOUR USERNAME',
    password = 'YOUR PASSWORD',
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping_verification_api.ShippingVerificationApi(api_client)
    company_code = "companyCode_example" # str | The company code of the company that recorded the transaction
    transaction_code = "transactionCode_example" # str | The transaction code to retrieve
    document_type = "SalesInvoice" # str | (Optional): The document type of the transaction to operate on. If omitted, defaults to \"SalesInvoice\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Evaluates a transaction against a set of direct-to-consumer shipping regulations and, if compliant, registers the transaction so that it may be included when evaluating regulations that span multiple transactions.
        api_response = api_instance.register_shipment_if_compliant(company_code, transaction_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ShippingVerificationApi->register_shipment_if_compliant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Evaluates a transaction against a set of direct-to-consumer shipping regulations and, if compliant, registers the transaction so that it may be included when evaluating regulations that span multiple transactions.
        api_response = api_instance.register_shipment_if_compliant(company_code, transaction_code, document_type=document_type)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ShippingVerificationApi->register_shipment_if_compliant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_code** | **str**| The company code of the company that recorded the transaction |
 **transaction_code** | **str**| The transaction code to retrieve |
 **document_type** | **str**| (Optional): The document type of the transaction to operate on. If omitted, defaults to \&quot;SalesInvoice\&quot; | [optional]

### Return type

[**ShippingVerifyResult**](ShippingVerifyResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A ShippingVerifyResult object. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Invalid Transaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_shipment**
> ShippingVerifyResult verify_shipment(company_code, transaction_code)

Evaluates a transaction against a set of direct-to-consumer shipping regulations.

The transaction and its lines must meet the following criteria in order to be evaluated: * The transaction must be recorded. Using a type of *SalesInvoice* is recommended. * A parameter with the name *AlcoholRouteType* must be specified and the value must be one of the following: '*DTC*', '*Retailer DTC*' * A parameter with the name *RecipientName* must be specified and the value must be the name of the recipient. * Each alcohol line must include a *ContainerSize* parameter that describes the volume of a single container. Use the *unit* field to specify one of the following units: '*Litre*', '*Millilitre*', '*gallon (US fluid)*', '*quart (US fluid)*', '*ounce (fluid US customary)*' * Each alcohol line must include a *PackSize* parameter that describes the number of containers in a pack. Specify *Count* in the *unit* field.  Optionally, the transaction and its lines may use the following parameters: * The *ShipDate* parameter may be used if the date of shipment is different than the date of the transaction. The value should be ISO-8601 compliant (e.g. 2020-07-21). * The *RecipientDOB* parameter may be used to evaluate age restrictions. The value should be ISO-8601 compliant (e.g. 2020-07-21). * The *PurchaserDOB* parameter may be used to evaluate age restrictions. The value should be ISO-8601 compliant (e.g. 2020-07-21). * The *SalesLocation* parameter may be used to describe whether the sale was made *OnSite* or *OffSite*. *OffSite* is the default value. * The *AlcoholContent* parameter may be used to describe the alcohol percentage by volume of the item. Specify *Percentage* in the *unit* field.  **Security Policies** This API depends on all of the following active subscriptions: *AvaAlcohol, AutoAddress, AvaTaxPro*

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import shipping_verification_api
from Avalara.SDK.model.shipping_verify_result import ShippingVerifyResult
from Avalara.SDK.model.error_details import ErrorDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = Avalara.SDK.Configuration(
    username = 'YOUR USERNAME',
    password = 'YOUR PASSWORD',
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping_verification_api.ShippingVerificationApi(api_client)
    company_code = "companyCode_example" # str | The company code of the company that recorded the transaction
    transaction_code = "transactionCode_example" # str | The transaction code to retrieve
    document_type = "SalesInvoice" # str | (Optional): The document type of the transaction to operate on. If omitted, defaults to \"SalesInvoice\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Evaluates a transaction against a set of direct-to-consumer shipping regulations.
        api_response = api_instance.verify_shipment(company_code, transaction_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ShippingVerificationApi->verify_shipment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Evaluates a transaction against a set of direct-to-consumer shipping regulations.
        api_response = api_instance.verify_shipment(company_code, transaction_code, document_type=document_type)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ShippingVerificationApi->verify_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_code** | **str**| The company code of the company that recorded the transaction |
 **transaction_code** | **str**| The transaction code to retrieve |
 **document_type** | **str**| (Optional): The document type of the transaction to operate on. If omitted, defaults to \&quot;SalesInvoice\&quot; | [optional]

### Return type

[**ShippingVerifyResult**](ShippingVerifyResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A ShippingVerifyResult object. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Invalid Transaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

