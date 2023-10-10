import mongoengine

class YourDocument(mongoengine.Document):
    id = mongoengine.StringField()
    source = mongoengine.StringField()
    description = mongoengine.StringField()
    is_active = mongoengine.BooleanField()

def get_source_url():
    mongoengine.connect("faas", host="mongodb://localhost:27017")
    document = YourDocument.objects(id="6524ec9adc1e70b6b860054a").first()

    if document:
        source_url = document.source
        is_active = document.is_active

        if is_active:
            return source_url
        else:
            print("The document is not active.")
    else:
        print("Document not found.")

source_url = get_source_url()
