from app import app, listeParties, idCompteurParties
from flask import request, json

@app.route('/parties', methods=['POST'])
def parties():
  global idCompteurParties

  if request.method == 'POST':
    partie = json.loads(request.data)
    partie['idPartie'] = idCompteurParties
    listeParties.append(partie)
    idCompteurParties = idCompteurParties + 1
    return json.dumps(partie, indent=2, sort_keys=True)


@app.route('/parties/<int:idPartie>', methods=['DELETE'])
def partiesId(idPartie):
  global idCompteurParties
  
  if request.method == 'DELETE':
    for partie in listeParties:
      if partie['idPartie'] == idPartie:
        listeParties.remove(partie)
        return json.dumps(partie, indent=2, sort_keys=True)
    return json.dumps({}, indent=2, sort_keys=True)
