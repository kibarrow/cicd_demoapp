from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        text = "Hello World!"
        return text

api.add_resource(HelloWorld, '/hello/world')

if __name__ == '__main__':
    # Runn Flask
    app.run(debug=True, host='0.0.0.0', port=int("5000"))
    # pass
    
    
    The build failed because we built the test BEFORE the feature. That's test driven development, and the failure is exactly what we want to see. When drone fails in the testing, the new container isn't built and published.

Build the Feature
    
    In your editor or IDE, open demoapp.py and add the new class and resource for HelloUniverse. You can simply copy and paste the below into your editor.

from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        text = "Hello World!"
        return text

api.add_resource(HelloWorld, '/hello/world')

class HelloUniverse(Resource):
    def get(self):
        text = "Hello Universe!"
        return text

api.add_resource(HelloUniverse, '/hello/universe')

if __name__ == '__main__':
    # Run Flask
    app.run(debug=True, host='0.0.0.0', port=int("5000"))
    
    Since we are NOT changing the actual build process stored in .drone.yml, we don't need to recreate the secrets file. Once the build process is complete, as long as new tests or steps aren't added these files can be left alone. Developers can focus on their code and changes, not the build process.
    
    Commit and push our updated application to begin the CICD process.
        
        # add the file to the git repo
        git add demoapp.py
            
            # commit the change
            git commit -m "Added hello/universe to the application"
                
                # push changes to GitHub
                git push

from flask import Flask, request from flask_restful import Resource, Api, reqparse app = Flask(__name__) app = Flask(__name__) api = Api(app) class HelloWorld(Resource): def get(self): text = "Hello World!" return text api.add_resource(HelloWorld, '/hello/world') class HelloUniverse(Resource): def get(self): text = "Hello Universe!" return text api.add_resource(HelloUniverse, '/hello/universe') if __name__ == '__main__': # Run Flask app.run(debug=True, host='0.0.0.0', port=int("5000"))
