from flask import Blueprint, request, jsonify
from Mongo2Client import Mongo2Client
from bson.objectid import ObjectId


joueur_bp = Blueprint('joueur', __name__)

mongo_client = Mongo2Client(db_name='pingpong')

@joueur_bp.route('/ajouter_joueur', methods=['POST'])
def ajouter_nouveau_joueur():
    data = request.get_json()
    resultat = mongo_client.db['joueur'].insert_one(data)

    if resultat.inserted_id:
        return jsonify({"succes": True, "id_insertion": str(resultat.inserted_id)}), 201
    else:
        return jsonify({"succes": False, "message": "Erreur lors de l'insertion"}), 500


@joueur_bp.route('/supprimer_joueur/<id_joueur>', methods=['POST'])
def supprimer_joueur(id_joueur):
    resultat = mongo_client.db['joueur'].delete_one({"_id": ObjectId(id_joueur)})

    if resultat.deleted_count == 1:
        return jsonify({"succes": True, "message": "Joueur supprimé avec succès"}), 200
    else:
        return jsonify({"succes": False, "message": "Joueur non trouvé ou déjà supprimé"}), 404



@joueur_bp.route('/liste_joueurs')
def liste_joueurs():
    joueurs = mongo_client.db['joueur'].find()
    liste_joueurs = [{"_id": str(joueur["_id"]), "nom": joueur.get("nom"), "prenom": joueur.get("prenom"), "age": joueur.get("age"), "sexe": joueur.get("sexe"), "categorie": joueur.get("categorie"), "point": joueur.get("point")} for joueur in joueurs]
    return jsonify(liste_joueurs)






@joueur_bp.route('/modifier_joueur/<id_joueur>', methods=['PUT'])
def modifier_joueur(id_joueur):
    data = request.form
    update_result = mongo_client.db['joueur'].update_one(
        {"_id": ObjectId(id_joueur)},
        {"$set": {
            "nom": data.get('nom'),
            "prenom": data.get('prenom'),
            "age": int(data.get('age')),
            "sexe": data.get('sexe'),
            "categorie": data.get('categorie'),
            "point": int(data.get('point'))
        }}
    )

    if update_result.modified_count == 1:
        return jsonify({"succes": True, "message": "Joueur modifié avec succès"}), 200
    else:
        return jsonify({"succes": False, "message": "Modification échouée ou joueur non trouvé"}), 400


@joueur_bp.route('/recherche_joueur/<id_joueur>', methods=['GET'])
def recherche_joueur(id_joueur):
    try:
        joueur = mongo_client.db['joueur'].find_one({"_id": ObjectId(id_joueur)})
        if joueur:
            joueur['_id'] = str(joueur['_id'])
            return jsonify(joueur), 200
        else:
            return jsonify({"message": "Joueur non trouvé"}), 404
    except Exception as e:
        return jsonify({"erreur": str(e), "message": "Erreur lors de la recherche du joueur"}), 400
