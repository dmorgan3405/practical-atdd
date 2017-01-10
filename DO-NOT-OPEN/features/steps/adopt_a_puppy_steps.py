from page_object import on, visit
from support.pages import DashboardPage
from support.pages import DetailsPage
from support.pages import ShoppingCartPage
from support.pages import CheckoutPage
from hamcrest import assert_that, contains_string


@given(u'I am looking for a puppy to adopt')
def step_impl(context):
    visit(DashboardPage)


@when(u'I view the details of the first puppy')
def step_impl(context):
    on(DashboardPage).view_details_for(1)


@when(u'I choose to adopt the puppy')
def step_impl(context):
    on(DetailsPage).adopt_me()
    on(ShoppingCartPage).complete_adoption()


@when(u'I adopt puppy {index}')
def step_impl(context, index):
    on(DashboardPage).view_details_for(int(index))
    on(DetailsPage).adopt_me()


@when(u'I choose to adopt another puppy')
def step_impl(context):
    on(ShoppingCartPage).continue_shopping()


@when(u'I choose to complete the adoption')
def step_impl(context):
    on(ShoppingCartPage).complete_adoption()


@when(u'I enter the name "{name}"')
def step_impl(context, name):
    on(CheckoutPage).set_name(name)


@when(u'I enter the address "{address}"')
def step_impl(context, address):
    on(CheckoutPage).set_address(address)


@when(u'I enter the contact email "{email}"')
def step_impl(context, email):
    on(CheckoutPage).set_email(email)


@when(u'I enter "{payment_method}" as the payment type')
def step_impl(context, payment_method):
    on(CheckoutPage).set_payment_method(payment_method)


@when(u'I checkout using')
def step_impl(context):
    on(CheckoutPage).checkout(context.table[0].as_dict())


@when(u'I checkout')
def step_impl(context):
    on(CheckoutPage).checkout()


@when(u'I checkout using a payment method of "{payment_method}"')
def step_impl(context, payment_method):
    on(CheckoutPage).checkout({'payment_method': payment_method})


@when(u'I place my order')
def step_impl(context):
    on(CheckoutPage).place_order()


@then(u'I should see the message "{text}"')
def step_impl(context, text):
    if text not in on(DashboardPage).html:
        raise Exception


@then(u'I should see "{text}"')
def step_impl(context, text):
    assert_that(on(DashboardPage).html, contains_string(text))
