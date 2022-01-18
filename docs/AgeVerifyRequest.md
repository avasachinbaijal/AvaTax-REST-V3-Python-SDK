# AgeVerifyRequest

The Request for the /ageVerification/verify endpoint. Describes information about the person whose age is being verified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**address** | [**AgeVerifyRequestAddress**](AgeVerifyRequestAddress.md) |  | [optional] 
**dob** | **str** | The value should be ISO-8601 compliant (e.g. 2020-07-21). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


