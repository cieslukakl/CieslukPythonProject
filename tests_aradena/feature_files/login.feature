#@web @login
Feature: Login to Aradena webiste
  As a web3 player,
  I want to login to aradena.io website,
  So I can start playing this amazing game.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario Outline: Successful Aradena page login
    Given I am on Aradena login page
    And I enter <Username> and <Password>
    When I select "Log in" button
    Then I see user home page

    Examples:
    |Username|Password|
    | ALK    | alk123 |

  Scenario Outline: Unsuccessful Aradena page login
    Given I am on Aradena login page
    And I enter <Username> and <Password>
    When I select "Log in" button
    Then I see login warning

    Examples:
    |Username|Password  |
    | ALK    |  123     |
    | ALK1   |  1231    |
    | ALK2   |  alk123  |