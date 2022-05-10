from app import app, listeEquipes, listeParties, idCompteurEquipes
from flask import request, json

@app.route('/equipes', methods=['GET'])
def equipes():
  if request.method == 'GET':
    return json.dumps(listeEquipes, indent=2, sort_keys=True)
  

@app.route('/equipes/<int:idEquipe>/parties', methods=['GET'])
def partiesEquipe(idEquipe):
  if request.method == 'GET':
    listePartiesEquipe = []
    for partie in listeParties:
      if partie['idEquipe'] == idEquipe:
        listePartiesEquipe.append(partie)
    return json.dumps(listePartiesEquipe, indent=2, sort_keys=True)


