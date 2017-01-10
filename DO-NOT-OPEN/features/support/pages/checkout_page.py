from page_object import PageObject


class CheckoutPage(PageObject):


    def define_elements(self):
        self.text_field(name='name', identifier={'id': 'order_name'})
        self.text_area(name='address', identifier={'id': 'order_address'})
        self.text_field(name='email', identifier={'id': 'order_email'})
        self.select_list(name='payment_method', identifier={'id': 'order_pay_type'})
        self.button(name='place_order', identifier={'css': '[value="Place Order"]'})

    CHECKOUT_DATA = {
        'name': 'Doug Morgan',
        'address': '510 North Street',
        'email': 'default@email.com',
        'payment_method': 'Check'
    }

    def checkout(self, overrides={}):
        merged = {**self.CHECKOUT_DATA, **overrides}

        self.set_name(merged['name'])
        self.set_address(merged['address'])
        self.set_email(merged['email'])
        self.set_payment_method(merged['payment_method'])
        self.place_order()
