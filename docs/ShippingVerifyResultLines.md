# ShippingVerifyResultLines


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_code** | **str** | Describes whether the line is compliant or not. In cases where a determination could not be made, resultCode will provide the reason why. | [optional] 
**line_number** | **str** | The lineNumber of the line evaluated. | [optional] 
**message** | **str** | A short description of the result of the checks made against this line. | [optional] 
**success_messages** | **str** | A detailed description of the result of each of the passed checks made against this line. | [optional] 
**failure_messages** | **str** | A detailed description of the result of each of the failed checks made against this line. | [optional] 
**failure_codes** | **[str]** | An enumeration of all the failure codes received for this line. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


