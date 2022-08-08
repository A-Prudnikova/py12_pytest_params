import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene import have


@pytest.fixture()
def desktop_fixture():
    browser.open('https://github.com/').driver.maximize_window()


@pytest.fixture()
def mobile_fixture():
    browser.open('https://github.com/')


def test_github_sign_in_desktop(desktop_fixture):
    s('[href="/login"]').click()
    s('.application-main ').should(have.text('Sign in to GitHub'))


def test_github_sign_in_mobile(mobile_fixture):
    s('[aria-label="Toggle navigation"]').click()
    s('[href="/login"]').click()
    s('.application-main ').should(have.text('Sign in to GitHub'))
