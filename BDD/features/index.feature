Feature: Static pages

    Scenario: Home page
        Given I access the url "http://127.0.0.1:8000/home/"
        Then I see the header "home"

    Scenario: Home page
        Given I access the url "http://127.0.0.1:8000/help/"
        Then I see the header "help"

    Scenario: Home page
        Given I access the url "http://127.0.0.1:8000/about/"
        Then I see the header "about"