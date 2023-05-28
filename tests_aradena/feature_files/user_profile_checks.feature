Feature: User profile attributes check
  As a web3 player,
  I want to check whether data on my profile is displayed correctly

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments


  Scenario: Warriors on quest is less or equal to army size
    Given I am logged in to Aradena
    When I enter profile page
    Then I see Warriors on quest amount is less or equal to Army size


  Scenario: All user attributes are displayed
    Given I am logged in to Aradena
    When I enter profile page
    Then I see all user attributes displayed