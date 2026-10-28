import unittest
from wsgiref.util import setup_testing_defaults
from router import application

class RouterTests(unittest.TestCase):
    def test_health_endpoint(self):
        environ = {}
        setup_testing_defaults(environ)
        environ["PATH_INFO"] = "/health"
        environ["REQUEST_METHOD"] = "GET"
        
        def start_response(status, headers):
            self.assertEqual(status, "200 OK")
            
        response = application(environ, start_response)
        self.assertEqual(b'{"ok": true}', response[0])

if __name__ == "__main__":
    unittest.main()
