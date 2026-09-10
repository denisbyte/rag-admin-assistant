"""
Métadonnées des documents administratifs utilisés par le RAG.

Chaque PDF local est associé à sa source officielle
sur le site Service-Public.gouv.fr.
"""

DOCUMENT_METADATA = {
    "01_demandes_titres_sejour_anef.pdf": {
        "title": "Faire une demande sur internet pour un titre de séjour, un changement de situation, un titre de voyage, une demande de naturalisation - ANEF",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/R59398",
    },
    "02_carte_resident_longue_duree_ue.pdf": {
        "title": "Carte de résident de longue durée-UE (étranger en France depuis 5 ans)",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F17359",
    },
    "03_vls_ts_visa_long_sejour.pdf": {
        "title": "Visa de long séjour (séjour de plus de 3 mois à 1 an)",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F16162",
    },
    "04_carte_sejour_etudiant.pdf": {
        "title": "Étudiant étranger en France : visa de long séjour ou titre de séjour",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F2231",
    },
    "05_changement_adresse_etranger.pdf": {
        "title": "Que doit faire un étranger en cas de changement d'adresse ?",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F35807",
    },
    "06_autorisation_travail_salarie_etranger.pdf": {
        "title": "Autorisation de travail d'un salarié étranger en France",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F2728",
    },
    "07_regroupement_familial.pdf": {
        "title": "Regroupement familial",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F11166",
    },
    "08_naturalisation_francaise_decret.pdf": {
        "title": "Naturalisation française par décret",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F15832",
    },
    "09_carte_sejour_vie_privee_familiale.pdf": {
        "title": "Carte de séjour \"vie privée et familiale\" d'un étranger en France",
        "url": "https://www.service-public.gouv.fr/particuliers/vosdroits/F2209",
    },
}