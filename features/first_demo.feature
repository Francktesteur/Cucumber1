Feature: Recherche sur DuckDuckGo
    # Demonstration de Feature Gherkin avec Python (Selenium + Behave)

    Scenario: Effectuer une recherche (valide)
        Given Je suis sur la page DuckDuckGo
        When Je saisis "Python Behave" dans la barre de Recherche
        And je valide la saisie avec la touche [Entrée]
        Then Je vois des résultats contenant "Python" # Valide

    Scenario: Effectuer une autre recherche (invalide)
        Given Je suis sur la page DuckDuckGo
        When Je saisis "Python Behave" dans la barre de Recherche
        And je valide la saisie avec la touche [Entrée]
        Then Je vois des résultats contenant "Zirgouflex"  # Invalide