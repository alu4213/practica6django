from lxml import html
from nose.tools import assert_equals
from lettuce import world, before, step
from lettuce.django import django_url
from django.test.client import Client

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I see the header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')[0]
    assert header.text == text