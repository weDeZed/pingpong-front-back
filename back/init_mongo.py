from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['pingpong']

# Collection 'equipe'
equipe_data = [
    {
        "_id": "id de l'équipe",
        "joueurs": [{"joueur": "joueur ..."}],
        "type": "type équipe"
    }
]
db.equipe.insert_many(equipe_data)

# Collection 'match'
match_data = [
    {
        "_id": "id match",
        "equipes": [
            {"équipe_1": "première équipe"},
            {"équipe_2": "deuxième équipe"}
        ],
        "table": "numéro de table",
        "date": "date du match",
        "heure": "heure du match",
        "résultat": "résultat du match à update"
    }
]
db.match.insert_many(match_data)

# Collection 'equipement_tournois'
equipement_tournois_data = [
    {
        "_id": "int",
        "table_tenis": [
            {"quantité": "number", "état": "string", "disponibilité": "string"}
        ],
        "filet": [
            {"quantité": "number", "état": "string", "disponibilité": "string"}
        ],
    }
]
db.equipement_tournois.insert_many(equipement_tournois_data)

# Collection 'tournois'
tournois_data = [
    {
        "_id": "int",
        "format": "string",
        "niveau": "string",
        "date": "date",
        "durée": "time",
        "lieu": "string",
        "match": [{"match": "match ..."}],
        "equipement_tournois": ""
    }
]
db.tournois.insert_many(tournois_data)

print("Collections et documents de base créés avec succès.")
