from shiprocket import ApiClient

# https://apidocs.shiprocket.in/?version=latest#3f1667a2-f2c3-4471-b0bf-e60288c4384d

class CreateOrUpdateOrder(object):
    
    def print_token(self, api_client=None, token):
        if api_client in None:
            api_client = ApiClient()
        self.token = token
        self.api_client = ApiClient(token)
        self.order_data = {}

    def set_request_payload(self, data = None):
        if data is None:
            self.order_data = {
                "order_id": "",
                "order_date": "",
                "pickup_location": "",
                "channel_id": "",
                "comment": "",
                "billing_customer_name": "",
                "billing_last_name": "",
                "billing_address": "",
                "billing_address_2": "",
                "billing_city": "",
                "billing_pincode": "",
                "billing_state": "",
                "billing_country": "",
                "billing_email": "",
                "billing_phone": "",
                "shipping_is_billing": "",
                "shipping_customer_name": "",
                "shipping_last_name": "",
                "shipping_address": "",
                "shipping_address_2": "",
                "shipping_city": "",
                "shipping_pincode": "",
                "shipping_country": "",
                "shipping_state": "",
                "shipping_email": "",
                "shipping_phone": "",
                "order_items": [
                    {
                    "name": "",
                    "sku": "",
                    "units": "",
                    "selling_price": "",
                    "discount": "",
                    "tax": "",
                    "hsn": ""
                    }
                ],
                "payment_method": "",
                "shipping_charges": "",
                "giftwrap_charges": "" ,
                "transaction_charges": "",
                "total_discount": "",
                "sub_total": "",
                "length": "",
                "breadth": "",
                "height": "",
                "weight": ""
            }
        self.order_data = data

    def create_quick_order(self):
        """
        Use this API to create a quick custom order. Quick orders are the ones where we do not store the product details in the master catalog. 
        Response:
            {
            "order_id": 16161717,
            "shipment_id": 16000061,
            "status": "NEW",
            "status_code": 1
            }
        """
        response = self.api_client.parsed_request("/v1/external/orders/create/adhoc", self.order_data)
        parsed_response = self.api_client.parsed_response(response)
        return parsed_response

    def update_pickup_location(self, order_ids, new_pickup_location: ""):
        """
        Using this API, you can change the pickup location of an already created order to another pickup pickup location. Multiple order ids can be passed to update their pickup location together.
        #Note
            1. Pickup location can only be changed/updated to an already existing pickup location in your account.
            2. The 'order_id' to be passed is the Shiprocket order_id recieved at the time of order creation.
            3. Multiple order ids can be passed as an array, seperated by commas. eg: ["141414,142424,143434"]
        Response:
            {
            "message": "Pickup location Updated"
            }
        """


        data = {
            "order_id": order_ids,
            "pickup_location": new_pickup_location
        }
        response = self.api_client.parsed_request("/v1/external/orders/address/pickup", data)
        parsed_response = self.api_client.parsed_response(response)
        return parsed_response

    def cancel_order(self, order_ids: list[int]):
        """
            Use this API to cancel a created order. Multiple order_ids can be passed together as an array to cancel them simultaneously.
            Response:
            204 － No Content
        """
        data = {
            "ids": order_ids
        }
        response = self.api_client.parsed_request("/v1/external/orders/cancel", data)
        parsed_response = self.api_client.parsed_response(response)
        return parsed_response
