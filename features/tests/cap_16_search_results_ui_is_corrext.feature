# Created by Zakhar at 12/13/2022
Feature: Test Scenario for Search results UI is correct

  Scenario: Verify: Search results UI is correct
    Given Open main page with search?q=cure
    Then Verify first results have name, image, and price