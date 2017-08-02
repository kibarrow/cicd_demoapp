import demoapp
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        demoapp.app.config['TESTING'] = True
        self.app = demoapp.app.test_client()

    def test_correct_http_response(self):
        resp = self.app.get('/hello/world')
        self.assertEquals(resp.status_code, 200)

    def test_correct_content(self):
        resp = self.app.get('/hello/world')
        self.assertEquals(resp.data, '"Hello World!"\n')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
import demoapp
import unittest


class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        demoapp.app.config['TESTING'] = True
        self.app = demoapp.app.test_client()
    
    def test_correct_http_response(self):
        resp = self.app.get('/hello/world')
        self.assertEquals(resp.status_code, 200)
    
    def test_correct_content(self):
        resp = self.app.get('/hello/world')
        self.assertEquals(resp.data, '"Hello World!"\n')
    
    def test_universe_correct_http_response(self):
        resp = self.app.get('/hello/universe')
        self.assertEquals(resp.status_code, 200)
    
    def test_universe_correct_content(self):
        resp = self.app.get('/hello/universe')
        self.assertEquals(resp.data, '"Hello Universe!"\n')
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
    Since we are NOT changing the actual build process stored in .drone.yml, we don't need to recreate the secrets file. Once the build process is complete, as long as new tests or steps aren't added these files can be left alone. Developers can focus on their code and changes, not the build process.
    
    Commit and push our updated test to begin the CICD process.
        
        # add the file to the git repo
        git add testing.py
            
            # commit the change
            git commit -m "Added new Tests for hello/universe"
                
                # push changes to GitHub
                git push

import demoapp import unittest class FlaskTestCase(unittest.TestCase): def setUp(self): demoapp.app.config['TESTING'] = True self.app = demoapp.app.test_client() def test_correct_http_response(self): resp = self.app.get('/hello/world') self.assertEquals(resp.status_code, 200) def test_correct_content(self): resp = self.app.get('/hello/world') self.assertEquals(resp.data, '"Hello World!"\n') def test_universe_correct_http_response(self): resp = self.app.get('/hello/universe') self.assertEquals(resp.status_code, 200) def test_universe_correct_content(self): resp = self.app.get('/hello/universe') self.assertEquals(resp.data, '"Hello Universe!"\n') def tearDown(self): pass if __name__ == '__main__': unittest.main()
