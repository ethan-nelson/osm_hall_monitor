from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Integer,
    SmallInteger,
    Text,
)

from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()

class History(Base):
    __tablename__ = 'history_all_changesets'
    id = Column(Integer, primary_key=True, nullable=False)
    changeset = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    timestamp = Column(Text, nullable=False)
    created = Column(Text)
    modified = Column(Text)
    deleted = Column(Text)

class History_Filters(Base):
    __tablename__ = 'history_filters'
    id = Column(Integer, primary_key=True, nullable=False)
    flag = Column(Integer, nullable=False)
    username = Column(Text, nullable=False)
    changeset = Column(BigInteger, nullable=False)
    timestamp = Column(Text, nullable=False)
    quantity = Column(Text, nullable=False)

class Watched_Users(Base):
    __tablename__ = 'watched_users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(Text, nullable=False)
    reason = Column(Text)
    author = Column(Text)
    authorid = Column(BigInteger)
    email = Column(Text)

class History_Users(Base):
    __tablename__ = 'history_users'
    id = Column(Integer, primary_key=True, nullable=False)
    wid = Column(Integer, nullable=False)
    userid = Column(BigInteger, nullable=False)
    changeset = Column(BigInteger, nullable=False)
    timestamp = Column(Text, nullable=False)
    created = Column(BigInteger)
    modified = Column(BigInteger)
    deleted = Column(BigInteger)

class Watched_Objects(Base):
    __tablename__ = 'watched_objects'
    id = Column(Integer, primary_key=True, nullable=False)
    element = Column(Text, nullable=False)
    reason = Column(Text)
    author = Column(Text)
    authorid = Column(BigInteger)
    email = Column(Text)

class History_Objects(Base):
    __tablename__ = 'history_objects'
    id = Column(Integer, primary_key=True, nullable=False)
    wid = Column(Integer, nullable=False)
    userid = Column(BigInteger, nullable=False)
    username = Column(Text, nullable=False)
    changeset = Column(BigInteger, nullable=False)
    timestamp = Column(Text, nullable=False)
    action = Column(SmallInteger, nullable=False)

class Watched_Keys(Base):
    __tablename__ = 'watched_keys'
    id = Column(Integer, primary_key=True, nullable=False)
    key = Column(Text, nullable=False)
    value = Column(Text, nullable=False)
    reason = Column(Text)
    author = Column(Text)
    authorid = Column(BigInteger)
    email = Column(Text)

class History_Keys(Base):
    __tablename__ = 'history_keys'
    id = Column(Integer, primary_key=True, nullable=False)
    wid = Column(Integer, nullable=False)
    userid = Column(BigInteger, nullable=False)
    key = Column(Text, nullable=False)
    value = Column(Text, nullable=False)
    element = Column(Text, nullable=False)
    username = Column(Text, nullable=False)
    changeset = Column(BigInteger, nullable=False)
    timestamp = Column(Text, nullable=False)
    action = Column(SmallInteger, nullable=False)

class File_List(Base):
    __tablename__ = 'file_list'
    id = Column(Integer, primary_key=True, nullable=False)
    sequence = Column(Text)
    timestamp = Column(Text)
    timetype = Column(Text)
    read = Column(Boolean)

class Whitelisted_Users(Base):
    __tablename__ = 'whitelisted_users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(Text, nullable=False)
    reason = Column(Text)
    author = Column(Text)
    authorid = Column(BigInteger)
