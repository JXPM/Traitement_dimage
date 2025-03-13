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
git commit -m "Ajout de mon TP5"
git push origin main

# library  
pip install opencv-python
pip install mediapipe


#Creation de dossier
mkdir TP1
mkdir TP2
mkdir TP3
mkdir TP4

#Creation de fichier 
touch TP1/TP1.py
touch TP1/TP1.ipynb
touch TP1/TP1_bis.ipynb
touch TP2/TP2.ipynb
touch TP3/TP3.ipynb
touch TP4/TP4.py
touch TP4/TP4_partie2.py

# Lancer dans le terminal le fichier TP4
python TP4/TP4.py
