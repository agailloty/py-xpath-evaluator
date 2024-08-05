# Python XPath Evaluator

XPath Evaluator est une application Tkinter qui permet de charger un fichier HTML et d'exécuter des requêtes XPath pour afficher les résultats.

## Fonctionnalités

- Chargement de fichiers HTML.
- Exécution de requêtes XPath sur le document chargé.
- Affichage des résultats des requêtes XPath dans une liste.
- Interface utilisateur simple et intuitive avec un arrière-plan blanc.
- Menu avec options pour ouvrir des fichiers et afficher des informations sur l'application.

## Captures d'écran

![Capture d'écran](screenshot.png)

## Installation

### Prérequis

- Python 3.x
- Tkinter (généralement inclus avec Python)
- lxml

### Étapes d'installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/agailloty/py-xpath-evaluator
    cd py-xpath-evaluator
    ```

2. Installez les dépendances :
    ```bash
    pip install lxml
    ```

## Utilisation

1. Exécutez l'application :
    ```bash
    python xpath_evaluator.py
    ```

2. Utilisez le menu "Fichier" pour ouvrir un fichier HTML.
3. Entrez une requête XPath dans le champ de texte.
4. Cliquez sur le bouton "Évaluer XPath" pour exécuter la requête et afficher les résultats dans la liste à droite de l'écran.

## Structure du Projet

- `xpath_evaluator.py` : Script principal de l'application.
- `README.md` : Ce fichier.
- `screenshot.png` : Capture d'écran de l'application (si disponible).

## Contribuer

Les contributions sont les bienvenues ! Pour proposer des améliorations, veuillez ouvrir une issue ou soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteurs

- Axel-Cleris Gailloty - [agailloty](https://gailloty.net)

---

Merci d'utiliser XPath Evaluator ! Si vous avez des questions ou des suggestions, n'hésitez pas à les partager.