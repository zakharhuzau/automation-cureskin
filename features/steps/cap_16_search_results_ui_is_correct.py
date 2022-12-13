from behave import given, then


@given('Open main page with {end_url}')
def open_page_with_end_url(context, end_url):
    context.app.search_page.open_page_with_end_url(end_url)


@then('Verify first results have name, image, and price')
def verify_1st_results_have_name_image_price(context):
    context.app.search_page.verify_1st_item_name()
    context.app.search_page.verify_1st_item_image()
    context.app.search_page.verify_1st_item_price()