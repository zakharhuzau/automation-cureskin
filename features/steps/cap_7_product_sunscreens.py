from behave import given, when, then


@given('Open main page')
def open_page(context):
    context.app.main_page.open_main_page()


@when('Click to "Shop by product"')
def click_to_shop_by_product(context):
    context.app.main_page.click_to_shop_by_product()


@when('Select Sunscreens')
def select_sunscreens(context):
    context.app.main_page.select_sunscreens()


@then('Verify "Sun Protection" header is shown')
def verify_sunprotection_header(context):
    context.app.sunprotection_page.verify_header()


@then('Verify the first product in sunscreen')
def verify_1st_product_in_sunscreen(context):
    context.app.sunprotection_page.verify_1st_product()