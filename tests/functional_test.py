import unittest
import http.client
import json

BASE_URL = "http://98.66.183.97"
PORT = 8088

class SimpleBookAppTests(unittest.TestCase):

    def test_home_page(self):
        """Vérifie que la page d'accueil est accessible."""
        connection = http.client.HTTPConnection(BASE_URL, PORT)
        connection.request("GET", "/")
        response = connection.getresponse()
        self.assertEqual(response.status, 200)
        connection.close()

    def test_create_book(self):
        """Vérifie qu'un livre peut être créé."""
        connection = http.client.HTTPConnection(BASE_URL, PORT)
        
        # Données du livre
        payload = {
            "title": "Mon Livre",
            "author": "Auteur Test"
        }
        headers = {"Content-Type": "application/json"}
        
        # Requête POST pour créer un livre
        connection.request("POST", "/books", body=json.dumps(payload), headers=headers)
        response = connection.getresponse()
        
        # Vérifie que le livre a été créé
        self.assertEqual(response.status, 201)

        # Lit la réponse et vérifie le contenu
        response_data = json.loads(response.read().decode())
        self.assertIn("id", response_data)
        self.assertEqual(response_data["title"], "Mon Livre")
        self.assertEqual(response_data["author"], "Auteur Test")
        
        connection.close()

if __name__ == "__main__":
    unittest.main()
