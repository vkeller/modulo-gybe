# modulo-gybe
Repo pour les séquences pédagogiques de l'éducation numérique (MODULO) de Vincent Keller

## Création du site modulo-gybe (sur githubpages)

- mettre à jour le repo avec les modifs
- mettre à jour la table des matières (_toc.yml)
- `git commit -m "blabla"`
- `git push`
- construire le jupyter book localement (cela prend du temps) : `jupyter-book  build .` depuis la racine
- vérifier localement qu'il est correct `firefox _build/html/index.html`
- uploader le résultat sur ghpages: `ghp-import -n -p -f _build/html`
- attendre 5 minutes et vérifier le résultat
- détruire le répertoire complet `rm -Rf _build`
