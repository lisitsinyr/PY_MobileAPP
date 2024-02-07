…or create a new repository on the command line
echo "# TEST" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:lisitsinyr/TEST.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin git@github.com:lisitsinyr/TEST.git
git branch -M main
git push -u origin main




git branch -m master main
git push -u origin main
# Теперь в настройках репозитория ставим по умолчанию новую ветку "main"
git push origin --delete master