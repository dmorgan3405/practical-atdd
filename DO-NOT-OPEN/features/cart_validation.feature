Feature: Shopping Cart Validation
  As a prospective puppy owner
  I want to see accessories that I may need for my puppy
  So that I am well equipped to care for it

  Background:
    Given I am looking for a puppy to adopt

  Scenario Outline: Shopping cart offers common accessories
    When I adopt puppy 1
    Then I should see "<accessory>" as an optional accessory
  Examples:
    | accessory       |
    | Collar & Leash  |
    | Chew Toy        |
    | Travel Carrier  |
    | First Vet Visit |

  Scenario: Validate cart with one puppy
    When I adopt puppy 1
    Then I should see "Brook" as the name for line item 1
    And I should see "$34.95" as the subtotal for line item 1
    And I should see "$34.95" as the total for the cart
