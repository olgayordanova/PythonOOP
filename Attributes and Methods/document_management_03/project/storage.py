class Storage:
    def __init__(self):
        self.categories  = []
        self.topics  = []
        self.documents  = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic) :
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        category = [el for el in self.categories if el.id == category_id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [el for el in self.topics if el.id == topic_id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = [el for el in self.documents if el.id == document_id][0]
        document.file_name = new_file_name

    def delete_category(self, category_id): #– delete the category with the provided id
        category = [el for el in self.categories if el.id == category_id][0]
        if category:
            self.categories.remove(category)


    def delete_topic(self, topic_id): # – delete the topic with the provided id
        topic = [el for el in self.topics if el.id == topic_id][0]
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id): # – delete the document with the provided id
        document = [el for el in self.documents if el.id == document_id][0]
        if document:
            self.documents.remove(document)

    def get_document(self, document_id): # – return the document with the provided id
        document = [el for el in self.documents if el.id == document_id][0]
        return document

    def __repr__( self): # – returns a string representation of each document on separate lines
        result = ""
        result += "\n".join(str(document) for document in self.documents)
        return result




