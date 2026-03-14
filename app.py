# Crée le fichier
touch app.py

# Ajoute le code de base Flask
echo "from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue dans IntrusionX !'

if __name__ == '__main__':
    app.run(debug=True)
" > app.py