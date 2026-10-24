from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, create_engine
from app.config import settings
from datetime import datetime


engine = create_engine(settings.DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(engine=engine, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, comment="主键ID")
    created_time:Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment="创建时间")
    updated_time:Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")





