from app import app, listeJoueurs,idCompteurJoueurs
from flask import request, json



@app.route('/joueurs', methods=['GET', 'POST'])
def joueurs():
  global idCompteurJoueurs
  if request.method == 'GET':
    print('Liste joueurs: ' + json.dumps(listeJoueurs, indent=2, sort_keys=True))
    return json.dumps(listeJoueurs, indent=2, sort_keys=True)
  
  if request.method == 'POST':
    request_data = json.loads(request.data)
    for joueur in request_data:
      print(joueur)
      joueur['idJoueur'] = idCompteurJoueurs
      listeJoueurs.append(joueur)
      idCompteurJoueurs = idCompteurJoueurs + 1
    print('Liste joueurs apres: ' + json.dumps(listeJoueurs, indent=2, sort_keys=True))
    return json.dumps(listeJoueurs, indent=2, sort_keys=True)

@app.route('/joueurs/<int:idJoueur>', methods=['PUT', 'DELETE'])
def joueursId(idJoueur):
  global idCompteurJoueurs
  if request.method == 'DELETE':
    for joueur in listeJoueurs:
      if joueur['idJoueur'] == idJoueur:
        listeJoueurs.remove(joueur)
        return json.dumps(joueur, indent=2, sort_keys=True)
    print(json.dumps(listeJoueurs, indent=2, sort_keys=True))
    return json.dumps({}, indent=2, sort_keys=True)

  if request.method == 'PUT':
    request_data = json.loads(request.data)
    print('liste joueurs avant' + json.dumps(listeJoueurs, indent=2, sort_keys=True))
    for joueur in listeJoueurs:
      if joueur['idJoueur'] == idJoueur:
        listeJoueurs.remove(joueur)
        listeJoueurs.append(request_data) # nouvelles donnees du joueur
        # return json.dumps(joueur, indent=2, sort_keys=True)
        break
    print('apres' + json.dumps(listeJoueurs, indent=2, sort_keys=True))
    return json.dumps({}, indent=2, sort_keys=True)

    


