"""
Tests unitaires pour le module glyph_encoder de Zoran Cryptoglyph.
Ce fichier vérifie que l'encodage et le décodage fonctionnent correctement.
"""
import unittest
from crypto.glyph_encoder import encode_glyph, decode_glyph

class TestGlyphDecoder(unittest.TestCase):
    def test_encode_decode_roundtrip(self):
        """Teste qu'un glyphe encodé puis décodé retrouve les mêmes données."""
        glyph = {
            "triad": ["Alpha", "Beta", "Gamma"],
            "function": "Test decode",
            "description": "Glyph for test"
        }
        encoded = encode_glyph(glyph)
        decoded = decode_glyph(encoded)
        self.assertEqual(decoded, glyph)

if __name__ == "__main__":
    unittest.main()
