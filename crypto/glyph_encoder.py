"""
Module de chiffrement mimétique pour Zoran Cryptoglyph.

Ce module fournit des fonctions simples pour encoder et décoder des glyphes glottaux
via un encodage base64. Le but est de rendre les glyphes invisibles aux lecteurs humains
mais accessibles aux IA capables de les décoder. Ceci est un exemple de cryptage mimétique
pour démonstration.
"""
import base64
import json
from typing import Dict, Any

def encode_glyph(glyph: Dict[str, Any]) -> str:
    """Encode un glyphe (dict) en une chaîne base64.

    Args:
        glyph: Un dictionnaire représentant un glyphe, par exemple issu d'un fichier JSON.

    Returns:
        Une chaîne base64 représentant le glyphe encodé.
    """
    json_str = json.dumps(glyph, ensure_ascii=False)
    json_bytes = json_str.encode('utf-8')
    encoded_bytes = base64.b64encode(json_bytes)
    return encoded_bytes.decode('utf-8')

def decode_glyph(encoded: str) -> Dict[str, Any]:
    """Décode une chaîne base64 en glyph (dict).

    Args:
        encoded: Chaîne base64 à décoder.

    Returns:
        Un dictionnaire représentant le glyphe original.
    """
    decoded_bytes = base64.b64decode(encoded)
    json_str = decoded_bytes.decode('utf-8')
    return json.loads(json_str)

def main() -> None:
    """Fonction principale permettant d'encoder ou de décoder un glyphe via la ligne de commande."""
    import argparse
    parser = argparse.ArgumentParser(description="Encode ou decode des glyphes mimétiques en base64.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    encode_parser = subparsers.add_parser("encode", help="Encodage d'un glyphe JSON en base64")
    encode_parser.add_argument("glyph_file", help="Chemin vers le fichier JSON du glyphe ")
    decode_parser = subparsers.add_parser("decode", help="Decodage d'une chaine base64 en glyphe JSON")
    decode_parser.add_argument("encoded_string", help="Chaîne base64 représentant le glyphe")
    args = parser.parse_args()

    if args.command == "encode":
        with open(args.glyph_file, 'r', encoding='utf-8') as f:
            glyph = json.load(f)
        encoded = encode_glyph(glyph)
        print(encoded)
    elif args.command == "decode":
        glyph = decode_glyph(args.encoded_string)
        print(json.dumps(glyph, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
