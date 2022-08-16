import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene import have

url = 'https://github.com'
sign_in = '[href="/login"'
toggle_nav = 'button[aria-label="Toggle navigation"'

chrome = pytest.fixture(params=[(460, 960), (1600, 992)])

@chrome
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def set_up_browser(browser_size):
    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open(url)


def test_github_sign_in_desktop():
    if browser._config.window_width < 1024:
        pytest.skip('Size for mobile version')

    s(sign_in).click()
    s('h1').should(have.exact_text('Sign in to GitHub'))



def test_github_sign_in_mobile():
    if browser._config.window_width > 1023:
        pytest.skip('Size for desktop version')

    s(toggle_nav).click()
    s(sign_in).click()
    s('h1').should(have.exact_text('Sign in to GitHub'))

