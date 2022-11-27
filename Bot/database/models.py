from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func


Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True)

    name = Column(String(40))
    username = Column(String(40), unique=True)

    ban = Column(Boolean, default=False)
    admin = Column(Boolean, default=False)

    def save(self):
        db.session.commit()
    
    def get_name(self):
        return '@' + self.username if self.username else self.name
        
    def __repr__(self):
        return "Users(chat_id={}, name={}, username={}, ban={}, admin={})".format(
            self.chat_id, self.name, self.username, self.ban, self.admin
        )
    
    def __str__(self):
        return "<code>{}</code> {} {}".format(
            self.chat_id, self.get_name(), "<b>ADMIN</b>" if self.admin else ""
        )


from Bot.database import db