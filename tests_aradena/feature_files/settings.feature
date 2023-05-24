#@web @search
Feature: Set user specific settings for my profile
  As a web3 player,
  I want to set up my personal profile,
  in a way other players can recognize me.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments


  Scenario: Successfull profile change
    Given I am logged in to Aradena
    And I enter tavern (Browse Warriors) page
    And I Filter By male or female
    And I input 1 random valid warior ID
    When I select Submit button
    Then I can see 1 warrior found
