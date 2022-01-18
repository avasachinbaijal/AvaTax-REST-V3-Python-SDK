# ShippingVerifyResult

The Response of the /shippingverify endpoint. Describes the result of checking all applicable shipping rules against each line in the transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliant** | **bool** | Whether every line in the transaction is compliant. | [optional] 
**message** | **str** | A short description of the result of the compliance check. | [optional] 
**success_messages** | **str** | A detailed description of the result of each of the passed checks made against this transaction, separated by line. | [optional] 
**failure_messages** | **str** | A detailed description of the result of each of the failed checks made against this transaction, separated by line. | [optional] 
**failure_codes** | **[str]** | An enumeration of all the failure codes received across all lines. | [optional] 
**warning_codes** | **[str]** | An enumeration of all the warning codes received across all lines that a determination could not be made for. | [optional] 
**lines** | [**[ShippingVerifyResultLines]**](ShippingVerifyResultLines.md) | Describes the results of the checks made for each line in the transaction. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


