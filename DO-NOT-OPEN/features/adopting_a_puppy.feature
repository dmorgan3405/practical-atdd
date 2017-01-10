Feature: Adopt A Puppy
  As an animal lover
  I want to adopt a puppy
  So that I can have a great companion and give a puppy a better life

  Background:
    Given I am looking for a puppy to adopt

  Scenario: Adopt One Puppy
    When I view the details of the first puppy
    And I choose to adopt the puppy
    And I enter the name "Jim Bob"
    And I enter the address "123 Main Street\nCleveland, OH 44113"
    And I enter the contact email "jimbob@atdd.com"
    And I enter "Check" as the payment type
    And I place my order
    Then I should see the message "Thank you for adopting a puppy!"

  Scenario: Adopting a puppy using a table
    When I view the details of the first puppy
    And I choose to adopt the puppy
    And I checkout using:
      | name           | address            | email           | payment_method |
      | Your Name Here | 1151 N Marginal Rd | you@example.com | Credit card    |
    Then I should see "Thank you for adopting a puppy!"

  Scenario: Adopting a puppy using default data
    When I view the details of the first puppy
    And I choose to adopt the puppy
    And I checkout
    Then I should see "Thank you for adopting a puppy!"

  Scenario: Adopting a puppy with a different payment method
    When I view the details of the first puppy
    And I choose to adopt the puppy
    And I checkout using a payment method of "Purchase order"
    Then I should see "Thank you for adopting a puppy!"
