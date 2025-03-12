#first commit on github
git init
git branch -M main
git add .
git commit -m "first commit"
gh repo create Traitement_dimage --public
git remote add origin https://github.com/JXPM/Traitement_dimage.git
git push --set-upstream origin main

#fichier Maj et push 
git status 
git add .
git commit -m "Maj TP3"
git push origin main

# library  

#Creation de fichier 
touch TP1/TP1.py
touch TP1/TP1.ipynb
touch TP1/TP1_bis.ipynb
touch TP2/TP2.ipynb
