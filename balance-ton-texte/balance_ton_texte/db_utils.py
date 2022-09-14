from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert
from sqlalchemy.orm import Session

# run docker with: sudo docker run -itd -e POSTGRES_USER=wym_admin -e 
        #POSTGRES_PASSWORD=admin -p 5432:5432 -v /data:/var/lib/postgresql/data --name postgresql postgres

# needed for creating a table with a pseudo-sql syntax
Base = declarative_base()
# engine declared as type://user:password@port:port/name
engine = create_engine('postgresql://wym_admin:admin@postgres:5432/postgres')
# no idea
meta=MetaData()
# sql = 'DROP TABLE IF EXISTS contact;'
# result = engine.execute(sql)
# Base.metadata.drop_all(engine)

class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    nom = Column(String(250), nullable=False)
    prenom = Column(String(250), nullable=False)
    tel = Column(String(16), nullable=True)
    email = Column(String(250), nullable=False)
    comm = Column(String(500), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "tel" : self.tel,
            "email" : self.email,
            "comm" : self.comm
        }

class Summary(Base):
    __tablename__ = 'summary'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    wc_text = Column(Integer, nullable=False) # len(text.split())
    summ = Column(String, nullable=True)
    wc_summ = Column(String, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "wc_text": self.wc_text,
            "summ" : self.summ,
            "wc_summ" : self.wc_summ
        }

meta.create_all(engine)
Base.metadata.create_all(engine)

def insert_contact(nom, prenom, tel, email, comm):
    with Session(engine) as session:
        session.begin()
        try:
            new_contact = Contact(nom=nom, prenom=prenom, tel=str(tel), email=email, comm=comm)
            session.add(new_contact)
        except:
            session.rollback()
            print('Rollback')
            raise
        else:
            print('commit')
            session.commit()


def insert_summary(text, summary):
    with Session(engine) as session:
        session.begin()
        try:
            new_text = Summary(text=text, wc_text=len(text.split()), summ=summary, wc_summ=len(summary.split()))
            session.add(new_text)
        except:
            session.rollback()
            print('Rollback')
            raise
        else:
            print('commit')
            session.commit()

# test
# insert_summary('bla bla bla', 'bla')