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

@pytest.mark.parametrize("browser_size", [(1600, 992)], indirect=True)
def test_github_desktop_indirect(browser_size):
    s(sign_in).click()
    s('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", [(460, 960)], indirect=True)
def test_github_mobile_indirect(browser_size):
    s(toggle_nav).click()
    s(sign_in).click()
    s('h1').should(have.exact_text('Sign in to GitHub'))