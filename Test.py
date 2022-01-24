import time
import Avalara.SDK
from Avalara.SDK.api import shipping_verification_api

print('Started')
configuration = Avalara.SDK.Configuration(
    username = '', 
    password = '',
    environment='sandbox'
)

with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping_verification_api.ShippingVerificationApi(api_client)
    try:
        api_instance.deregister_shipment("Default","dededed")
        print('Success')
    except Avalara.SDK.ApiException as e:
        print("Exception when calling AgeVerificationApi->verify_age: %s\n" % e)

print("Completed")