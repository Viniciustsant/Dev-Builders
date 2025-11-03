from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum, func

Base = declarative_base()

class UserRole(str, Enum):
  ADMIN = "ADMIN"
  USER = "USER"

class User(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String, unique=True, nullable=False)  
  password_hash = Column(String, nullable=False)
  role = Column(SQLEnum(UserRole), nullable=False)
  created_at = Column(DateTime, server_default=func.now())
