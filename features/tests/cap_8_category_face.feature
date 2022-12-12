# Created by Zakhar at 12/12/2022
Feature: Test Scenario for User can shop by category Face

  Scenario: Verify: User can shop by category Face
    Given Open main page
    When Click to "Shop by category"
    And Select Face
    Then Verify "Face" header is shown
    And Verify the first product in face