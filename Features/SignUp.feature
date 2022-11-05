Feature: AA User i want to sign up

  Scenario: En tant que user je veux connecter au site
    Given Launch chrome browser
    When le site est lancé
    Then Ouvrir le popup de connexion
    And Remplir les champs avec un email "Email" et un mot de passe "Password"
    Then Clicker sur le boutton Se connecter
    Then User est connecté avec succès
    And Fermer le browser

  Scenario Outline:
    Given Launch chrome browser
    When le site est lancé
    Then Ouvrir le popup de connexion
    And Remplir les champs avec un email "<Email>" et un mot de passe "<Password>"
    Then Clicker sur le boutton Se connecter
    Then User est connecté avec succès
    And Fermer le browser
    Examples:
      | Email                       | Password     |
      | mohamedbenfredj91@gmail.com | Chuila_0010. |
      | amin29    | Amin29       |
