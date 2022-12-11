# Created by Zakhar at 12/8/2022
Feature: Test Scenario for User can shop by product Sunscreens

  Scenario: Verify: User can shop by product Sunscreens
    Given Open main page
    When Click to "Shop by product"
    And Select Sunscreens
    Then Verify "Sun Protection" header is shown
    And Verify the first product in sunscreen