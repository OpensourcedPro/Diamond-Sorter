from sqlalchemy import create_engine, Column, String, Integer,Boolean,Text,ForeignKey,UniqueConstraint,CheckConstraint,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import SQLAlchemyError
import time
Base = declarative_base()
class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_table(self):
        try:
            Base.metadata.create_all(self.engine)
        except SQLAlchemyError as e:
            print(f"Error creating tables: {e}")

    def insert(self, table, **kwargs):
        session = self.Session()
        isok = True
        try:
            record = table(**kwargs)
            session.add(record)
            session.commit()
        except SQLAlchemyError as e:
            print(f"Error inserting record: {e}")
            session.rollback()
            isok = False
        finally:
            session.close()
        return isok
    def query(self, table, *args,order_by=None,**kwargs):
        session = self.Session()
        try:
            query = session.query(table).filter_by(**kwargs).filter(*args)
            if order_by is not None:
                query = query.order_by(order_by)
            result = query.all()
            return result
        except SQLAlchemyError as e:
            print(f"Error querying record: {e}")
            return None
        finally:
            session.close()
    def update(self, table, filter_by, **kwargs):
        session = self.Session()
        isok = True
        try:
            record = session.query(table).filter_by(**filter_by).first()
            if record:
                for key, value in kwargs.items():
                    setattr(record, key, value)
                session.commit()
            else:
                isok = False
                print("Record not found for update.")
        except SQLAlchemyError as e:
            isok=False
            print(f"Error updating record: {e}")
            session.rollback()
        finally:
            session.close()
        return isok
    def delete(self, table, **kwargs):
        session = self.Session()
        isok = True
        try:
            record = session.query(table).filter_by(**kwargs).first()
            if record:
                session.delete(record)
                session.commit()
            else:
                print("Record not found for delete.")
        except SQLAlchemyError as e:
            isok=False
            print(f"Error deleting record: {e}")
            session.rollback()
        finally:
            session.close()
        return isok

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)  # replaced password with password_hash
    nickname = Column(String(80), nullable=True)
    lastip = Column(String(45), nullable=True)  # adjusted size for IPv6 compatibility
    last_online = Column(Integer, default=lambda: int(time.time()))
    isdeleted = Column(Boolean, default=False)
    avatar = Column(String(256), nullable=True)
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
class ChatGroup(Base):
    __tablename__ = 'chat_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    manager_id = Column(Integer, ForeignKey('user.id'), nullable=False)
class GroupMembers(Base):
    __tablename__ = 'group_members'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('chat_group.id', ondelete='CASCADE'), nullable=False)


class Friendship(Base):
    __tablename__ = 'friendship'
    id = Column(Integer, primary_key=True)
    user1_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user2_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    __table_args__ = (UniqueConstraint('user1_id', 'user2_id', name='unique_friendship'),)

    

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    timestamp = Column(Integer, default=lambda: int(time.time()))
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('chat_group.id', ondelete='CASCADE'), nullable=True)
    friendship_id = Column(Integer, ForeignKey('friendship.id', ondelete='CASCADE'), nullable=True)

    # Add constraints to ensure that a message is either from a group or a friendship, not both.
    __table_args__ = (
        CheckConstraint(
            '(group_id IS NULL AND friendship_id IS NOT NULL) OR (group_id IS NOT NULL AND friendship_id IS NULL)',
            name='message_source_check'
        ),
    )
import enum
class OperationType((enum.Enum)):
    ADD_FRIEND = 1
    REMOVE_FRIEND = 2
    CREATE_GROUP = 3
    DELETE_GROUP = 4
    ADD_GROUP_MEMBER = 5
    REMOVE_GROUP_MEMBER = 6
    LEAVE_GROUP = 7
    JOIN_GROUP = 8
    RENAME_GROUP = 9
    ACCEPT_FRIEND = 10
    ACCEPT_GROUP = 11
class Operation(Base):
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(OperationType), nullable=False)
    timestamp = Column(Integer, default=lambda: int(time.time()))
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('chat_group.id'), nullable=True)
    friend_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    isProcess = Column(Boolean,default=False)
    __table_args__ = (
        CheckConstraint(
            '(group_id IS NULL AND friend_id IS NOT NULL) OR (group_id IS NOT NULL AND friend_id IS NULL)',
            name='operation_source_check'
        ),
    )