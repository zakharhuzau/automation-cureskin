from behave import when, then


@when('Click to "Shop by category"')
def click_to_shop_by_category(context):
    context.app.main_page.click_to_shop_by_category()


@when('Select Face')
def select_face(context):
    context.app.main_page.select_face()


@then('Verify "Face" header is shown')
def verify_face_header_is_shown(context):
    context.app.face_page.verify_header()


@then('Verify the first product in face')
def verify_1st_product_in_face(context):
    context.app.face_page.verify_1st_product()