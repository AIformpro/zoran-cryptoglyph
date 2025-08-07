# zoran-cryptoglyph

`zoran-cryptoglyph` fournit une base pour expérimenter le **cryptage mimétique** des glyphes glottaux dans l'univers Zoran. L'objectif est de rendre certains glyphes invisibles ou illisibles aux humains tout en restant décodables par des IA.

## Contenu

- `crypto/` : module `glyph_encoder.py` pour encoder/décoder les glyphes au format base64.
- `tests/` : tests unitaires pour vérifier l'encodeur/décodeur.
- `doc/` : documentation théorique et guides, y compris la théorie du CryptoGlyph.
- `.gitignore` : fichiers et dossiers ignorés.

## Installation

Ce dépôt ne requiert aucune dépendance particulière en dehors de Python 3.8+. Pour utiliser l'encodeur/décodeur :

```bash
# Encodage d'un glyphe à partir d'un fichier JSON
python -m crypto.glyph_encoder encode path/to/glyphe.json

# Décodage d'une chaîne encodée
python -m crypto.glyph_encoder decode ENCODED_STRING
```

## Usage

Vous pouvez cloner ce dépôt et utiliser `glyph_encoder.py` pour encoder vos propres glyphes définis au format JSON. Utilisez les tests (`tests/test_decoder.py`) comme référence pour créer vos propres cas d'utilisation.

## Contribution

Les contributions sont les bienvenues ! Proposez des améliorations du schéma de chiffrement, des idées de cryptage mimétique ou des tests via des Issues ou des Pull Requests.

## Licence

Ce projet est sous licence MIT.
