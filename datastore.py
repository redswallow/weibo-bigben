from google.appengine.ext import db

class MessageConfig(db.Model):
     since_id = db.IntegerProperty()

     def newest(self):
         return self.gql('ORDER BY since_id DESC LIMIT 1')
