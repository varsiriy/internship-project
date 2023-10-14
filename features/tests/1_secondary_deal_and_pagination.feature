Feature: Test for Secondary deal page and Pagination

  Scenario: User can open the Secondary deals page and go through the pagination
    Given Open the main page
    And Log in to the page
    When Click on Secondary option at the left side menu
    Then Verify the right page opens
    And  Go to the final page using the pagination button
    And Go back to the first page using the pagination button