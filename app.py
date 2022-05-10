from flask import Flask, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

idCompteurJoueurs = 100
listeJoueurs = [
  { 'idJoueur': 1, 'numero': 5, 'position': 'QB', 'prenom': 'Etienne', 'nom': 'Penelle' }, 
  { 'idJoueur': 2, 'numero': 52, 'position': 'DB', 'prenom': 'Juan-Sebastian', 'nom': 'Burgos-Rincon' }, 
  { 'idJoueur': 3, 'numero': 88, 'position': 'R', 'prenom': 'Vincent', 'nom': 'Lanoie' }, 
  { 'idJoueur': 4, 'numero': 69, 'position': 'DL', 'prenom': 'Benjamin', 'nom': 'Savage' }, 
  { 'idJoueur': 5, 'numero': 64, 'position': 'OL', 'prenom': 'Kevin', 'nom': 'Paquette' }, 
  { 'idJoueur': 6, 'numero': 6, 'position': 'RB', 'prenom': 'William', 'nom': 'Grondin' },
  { 'idJoueur': 7, 'numero': 51, 'position': 'LB', 'prenom': 'Francis', 'nom': 'Benoit' },
  { 'idJoueur': 8, 'numero': 67, 'position': 'LB', 'prenom': 'Etienne', 'nom': 'Roy' }
]

idCompteurEquipes = 100
listeEquipes = [
  { 'idEquipe': 1, 'niveau': 'Juvénile', 'annee': '2022'},
  { 'idEquipe': 2, 'niveau': 'Cadet', 'annee': '2022'},
  { 'idEquipe': 3, 'niveau': 'Benjamin', 'annee': '2022'}
]

idCompteurParties = 100
listeParties = [
  {'idPartie': 1, 'idEquipe': 1, 'adversaire': 'Fernand-Lefebvre', 'date': '2022-10-01' },
  {'idPartie': 2, 'idEquipe': 1, 'adversaire': 'College St-Bernard', 'date': '2022-10-08' },
  {'idPartie': 3, 'idEquipe': 1, 'adversaire': 'Marie-Rivier', 'date': '2022-10-15' },

  {'idPartie': 4, 'idEquipe': 2, 'adversaire': 'Fernand-Lefebvre', 'date': '2022-10-01' },
  {'idPartie': 5, 'idEquipe': 2, 'adversaire': 'College St-Bernard', 'date': '2022-10-08' },
  {'idPartie': 6, 'idEquipe': 2, 'adversaire': 'Marie-Rivier', 'date': '2022-10-15' },

  {'idPartie': 7, 'idEquipe': 3, 'adversaire': 'Fernand-Lefebvre', 'date': '2022-10-01' },
  {'idPartie': 8, 'idEquipe': 3, 'adversaire': 'College St-Bernard', 'date': '2022-10-08' },
  {'idPartie': 9, 'idEquipe': 3, 'adversaire': 'Marie-Rivier', 'date': '2022-10-15' },
]


@app.route("/")
def hello_world():
  message = {
    'body': 'Hello World!'
  }
  return json.dumps(message, indent=2, sort_keys=True)

import routes.joueurs_routes
import routes.equipes_routes
import routes.parties_routes