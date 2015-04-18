from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.database', echo=True)

Base = declarative_base()


from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     password = Column(String)

#     def __repr__(self):
#        return "<User(name='%s', fullname='%s', password='%s')>" % (
#                             self.name, self.fullname, self.password)


class Stratop(Base):
    __tablename__ = 'stratop'
    id = Column(Integer, primary_key=True)
    constellation = Column(String)
    good_guys = Column(String)

class Battle(Base):
    __tablename__ = 'battle'
    id = Column(Integer, primary_key=True)
    stratop = Column(Integer, ForeignKey('stratop.id'))
    system_name = Column(String)
    structure_name = Column(String)

class ControlNode(Base):
    __tablename__ = 'controlnode'
    id = Column(Integer, primary_key=True)
    battle = Column(Integer, ForeignKey('battle.id'))
    system_name = Column(String)
    control = Column(String)

class CorpStatus(Base):
    __tablename__ = 'corpstatus'
    id = Column(Integer, primary_key=True)
    corp = Column(String)
    number = Column(Integer)
    stratop = Column(Integer, ForeignKey('stratop.id'))

class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    time = Column(Date)
    stratop = Column(Integer, ForeignKey('stratop.id'))
    text = Column(String)

class System(Base):
    __tablename__ = 'system'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    stratop = Column(Integer, ForeignKey('stratop.id'))

class SystemCorps(Base):
    __tablename__ = 'systemcorps'
    id = Column(Integer, primary_key=True)
    corp = Column(String)
    system = Column(Integer, ForeignKey('system.id'))
    number = Column(Integer)


# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

