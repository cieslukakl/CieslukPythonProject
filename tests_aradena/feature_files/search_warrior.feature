Feature: Search for specific warrior in tavern
  As a web3 player,
  I want to search specific warriror in tavern,
  So I can browse characters of potential enemies.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario Outline: Successfull search for warrior in tavern
    Given I am logged in to Aradena
    And I enter tavern (Browse Warriors) page
    And I select Filter By <collection>
    And I input warrior <warriorId>
    When I select Submit button
    Then I can see <number> of warriors found for <collection> with <warriorId>

    Examples:
    |collection    |warriorId|number|
  | Male           | 0       | 1 |
  | Female         | 1       | 1 |
  | AllCollections | 5199    | 2 |
  | AllCollections | 6000    | 1 |
  | AllCollections | 7999    | 1 |

  Scenario Outline: Unsuccessful search for warrior in tavern
    Given I am logged in to Aradena
    And I enter tavern (Browse Warriors) page
    And I select Filter By <collection>
    And I input warrior <warriorId>
    When I select Submit button
    Then I can see "No warriors found" message

    Examples:
    |collection        |warriorId |
    | AllCollections   | -1       |
    | AllCollections   | 8000     |
    | Female           | 6000     |


  Scenario: Successfull search for warrior in tavern (RANDOM)
    Given I am logged in to Aradena
    And I enter tavern (Browse Warriors) page
    And I Filter By male or female
    And I input 1 random valid warior ID
    When I select Submit button
    Then I can see 1 warrior found
