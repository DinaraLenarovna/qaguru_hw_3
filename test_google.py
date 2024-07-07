from selene import browser, be, have


def test_google_pass(open_browser):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_incorrect(open_browser):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('jhbjfnlkstjnktjms').press_enter()
    browser.element('#botstuff').should(have.text('Your search - jhbjfnlkstjnktjms - did not match any documents.'))





