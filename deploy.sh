# 1. Build local
jupyter-book build .
jupyter-book build .

# 2. Ajouter le CNAME localement
echo "cours.vkeller.info" > _build/html/CNAME

# 3. Push avec ghp-import
ghp-import -n -p -f _build/html
