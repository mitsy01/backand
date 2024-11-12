from sqlalchemy import String, create_engine
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, DeclarativeBase


engine = create_engine("sqlite:///restoraunt.db", echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Restoraunt(Base):
    __tablename__ = "restourant"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(String(65))
    comp_dish: Mapped[str] = mapped_column(String())
    

def create_db():
    Base.metadata.create_all(bind=engine)