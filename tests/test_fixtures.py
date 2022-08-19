import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene import have

url = 'https://github.com'
sign_in = '[href="/login"'
toggle_nav = 'button[aria-label="Toggle navigation"'


@pytest.fixture(scope='function', params=[(1600, 992)])
def set_up_browser_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    browser.open(url)


def test_github_desktop_parametrize(set_up_browser_desktop):
    s(sign_in).click()
    s('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.fixture(scope='function', params=[(460, 960)])
def set_up_browser_mobile(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    browser.open(url)


def test_github_mobile_parametrize(set_up_browser_mobile):
    s(toggle_nav).click()
    s(sign_in).click()
    s('h1').should(have.exact_text('Sign in to GitHub'))