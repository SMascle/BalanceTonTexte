from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert
from sqlalchemy.orm import Session

Base = declarative_base()
engine = create_engine('postgresql://baeldung:baeldung@localhost:5432/postgres')
meta=MetaData()

class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    nom = Column(String(250), nullable=False)
    prenom = Column(String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom
        }
meta.create_all(engine)
Base.metadata.create_all(engine)
print(Contact.__table__)
print(Contact.__mapper__)

with Session(engine) as session:
    session.begin()
    try:
        new_contact = Contact(nom="test", prenom="Pinco")
        session.add(new_contact)
    except:
        session.rollback()
        raise
    else:
        session.commit()
