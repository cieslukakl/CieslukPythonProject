Feature: Set user specific settings for my profile
  As a web3 player,
  I want to set up my personal profile,
  in a way other players can recognize me.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments


  Scenario: Successfull personal bio change
    Given I am logged in to Aradena
    And I enter profile page
    And I select Settings icon
    And I input faker values for Personal bio
    When I select Save button
    Then I can see Success notification
    And Personal bio is updated on profile page

