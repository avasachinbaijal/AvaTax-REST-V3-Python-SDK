import time
import Avalara.ASV
from Avalara.ASV.api import shipping_verification_api

print('Started')
configuration = Avalara.ASV.Configuration(
    username = 'demo.compliance-verification', 
    password = 'sxgv7KK4HX*B7vY@',
    environment='sandbox'
)

with Avalara.ASV.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shipping_verification_api.ShippingVerificationApi(api_client)
    try:
        api_instance.deregister_shipment("Default","dededed")
        print('Success')
    except Avalara.ASV.ApiException as e:
        print("Exception when calling AgeVerificationApi->verify_age: %s\n" % e)

print("Completed")