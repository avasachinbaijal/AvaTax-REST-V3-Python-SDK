# ErrorDetailsErrorDetails

Message Details Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Name of the error or message. | [optional] 
**message** | **str** | Concise summary of the message, suitable for display in the caption of an alert box. | [optional] 
**number** | **int** | Unique ID number referring to this error or message. | [optional] 
**description** | **str** | A more detailed description of the problem referenced by this error message, suitable for display in the contents area of an alert box. | [optional] 
**fault_code** | **str** | Indicates the SOAP Fault code, if this was related to an error that corresponded to AvaTax SOAP v1 behavior. | [optional] 
**help_link** | **str** | URL to help for this message | [optional] 
**severity** | **str** | Severity of the message | [optional]  if omitted the server will use the default value of "Error"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


