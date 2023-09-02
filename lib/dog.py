from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog_id, new_breed):
    dog = session.query(Dog).filter_by(id=dog_id).first()
    if dog:
        dog.breed = new_breed
        session.commit()
    else:
        # Handle the case where the dog with the specified ID is not found.
        raise Exception("Dog not found")
