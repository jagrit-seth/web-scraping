import mongoengine
from bson.objectid import ObjectId
from mongoengine import Document, ObjectIdField, DictField, StringField, BooleanField, EmbeddedDocument, \
    EmbeddedDocumentField


class YourDocument(Document):
    class Description(EmbeddedDocument):
        description = StringField()
        type = StringField()
        url = StringField()

    _id = ObjectIdField(required=True, default=ObjectId)
    source = EmbeddedDocumentField(Description)
    is_active = BooleanField()

    meta = {
        'collection': 'Test'
    }


def get_source_url():
    mongoengine.connect("faas", host="mongodb://localhost:27017")
    documents = YourDocument.objects(is_active=True)
    urls = [doc.source.url for doc in documents]
    return urls


source_url = get_source_url()
