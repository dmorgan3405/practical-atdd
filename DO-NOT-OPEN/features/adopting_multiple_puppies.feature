Feature: Adopting multiple puppies

  As a puppy lover
  I want to adopt multiple puppies
  So that ...

  Background:
    Given I am looking for a puppy to adopt

  Scenario: Adopting multiple puppies
    When I adopt puppy 1
    And I choose to adopt another puppy
    And I adopt puppy 2
    And I choose to complete the adoption
    And I checkout
    Then I should see "Thank you for adopting a puppy!"
