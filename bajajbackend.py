import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('gateactivities.json')
firebase_admin.initialize_app(cred)
# Get a reference to the Firestore database
db = firestore.client()

# Reference a specific collection
collection_ref = db.collection('Attendance')

# Retrieve all documents in the collection
docs = collection_ref.get()
#print(type(docs))


# Process the retrieved documents
lis=[]
p=0
for doc in docs:
    #print(f'Document ID: {doc.id}')
    lis.insert(p,doc.id)
    p+=1
    #print(f'Document Data: {doc.to_dict()}')
    print('---')
    print(doc.id)
    print('---')

    doc_ref1 = db.collection('Attendance').document(doc.id)


    doc1 = doc_ref1.get()

    field_names = doc1.to_dict().keys()
    #print(field_names)

    for field_name in field_names:
        #print(field_name)

        if field_name=='idd':
            continue
        elif field_name=='aadhaar':
            continue
        elif field_name=='address':
            continue
        elif field_name=='date':
            continue
        elif field_name=='id':
            continue
        elif field_name=='status':
            continue
        elif field_name=='time':
            continue
        
        field_value = doc.get(field_name)
        print(f"{field_name}:\t{field_value}")
#print(lis)


