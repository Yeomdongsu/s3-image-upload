from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.posting import PostingResource  
from resources.image import FileUploadResource
from resources.rekognition import ObjectDetectionResource

app = Flask(__name__)

# 환경변수 세팅
app.config.from_object(Config)
# JWT 매니저를 초기화
jwt = JWTManager(app)

api = Api(app)

api.add_resource(FileUploadResource, "/upload")
api.add_resource(PostingResource, "/posting")
api.add_resource(ObjectDetectionResource, "/object_detection")

if __name__ == "__main__" :
    app.run()