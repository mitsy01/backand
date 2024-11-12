from db import Restoraunt, Session


def add_dish(owner, comp_dish):
    with Session() as session:
        restourant = Restoraunt(owner=owner, comp_dish=comp_dish)
        session.add(restourant)
        session.commit()
        session.refresh(restourant)
        return restourant.id
    
    
def get_restourants():
    with Session() as session:
        return session.query(Restoraunt).all()
    

def get_restourant():
    with Session() as session:
        return session.query(Restoraunt).where(Restoraunt.id == id).first()
    

def update_restourant(id, owner, comp_dish):
    with Session() as session:
        restourant = session.query(Restoraunt).filter_by(id=id).first()
        restourant.owner = owner
        restourant.comp_dish = comp_dish
        session.commit()
        return "Інформація про ресторан оновленна"
    

def del_restourant(id):
     with Session() as session:
        restourant = session.query(Restoraunt).filter_by(id=id).first()
        session.delete(restourant)
        session.commit()
        return "Інформацію про ресторан видалено"