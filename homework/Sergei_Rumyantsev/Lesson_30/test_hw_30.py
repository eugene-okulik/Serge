from playwright.sync_api import Page, expect, Route
import json


def test_applephonepro17(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 17 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route('**/step0_iphone/**', handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator("h3.rf-hcard-content-title").filter(has_text="iPhone 17 Pro Max").first.click()
    title = page.locator('#rf-digitalmat-overlay-label-0').first
    expect(title).to_contain_text('яблокофон 17 про')
