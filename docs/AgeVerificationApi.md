# Avalara.SDK.AgeVerificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_age**](AgeVerificationApi.md#verify_age) | **POST** /api/v2/ageverification/verify | Determines whether an individual meets or exceeds the minimum legal drinking age.


# **verify_age**
> AgeVerifyResult verify_age(age_verify_request)

Determines whether an individual meets or exceeds the minimum legal drinking age.

The request must meet the following criteria in order to be evaluated: * *firstName*, *lastName*, and *address* are required fields. * One of the following sets of attributes are required for the *address*:   * *line1, city, region*   * *line1, postalCode*  Optionally, the transaction and its lines may use the following parameters: * A *DOB* (Date of Birth) field. The value should be ISO-8601 compliant (e.g. 2020-07-21). * Beyond the required *address* fields above, a *country* field is permitted   * The valid values for this attribute are [*US, USA*]  **Security Policies** This API depends on the active subscription *AgeVerification*

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import age_verification_api
from Avalara.SDK.model.age_verify_result import AgeVerifyResult
from Avalara.SDK.model.age_verify_failure_code import AgeVerifyFailureCode
from Avalara.SDK.model.age_verify_request import AgeVerifyRequest
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
    api_instance = age_verification_api.AgeVerificationApi(api_client)
    age_verify_request = AgeVerifyRequest(
        first_name="first_name_example",
        last_name="last_name_example",
        address=AgeVerifyRequestAddress(
            line1="line1_example",
            city="city_example",
            region="region_example",
            country="US",
            postal_code="postal_code_example",
        ),
        dob="dob_example",
    ) # AgeVerifyRequest | Information about the individual whose age is being verified.
    simulated_failure_code = AgeVerifyFailureCode("not_found") # AgeVerifyFailureCode | (Optional) The failure code included in the simulated response of the endpoint. Note that this endpoint is only available in Sandbox for testing purposes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Determines whether an individual meets or exceeds the minimum legal drinking age.
        api_response = api_instance.verify_age(age_verify_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling AgeVerificationApi->verify_age: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Determines whether an individual meets or exceeds the minimum legal drinking age.
        api_response = api_instance.verify_age(age_verify_request, simulated_failure_code=simulated_failure_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling AgeVerificationApi->verify_age: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **age_verify_request** | [**AgeVerifyRequest**](AgeVerifyRequest.md)| Information about the individual whose age is being verified. |
 **simulated_failure_code** | **AgeVerifyFailureCode**| (Optional) The failure code included in the simulated response of the endpoint. Note that this endpoint is only available in Sandbox for testing purposes. | [optional]

### Return type

[**AgeVerifyResult**](AgeVerifyResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An AgeVerificationResult object. |  -  |
**400** | Invalid Request Model |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

