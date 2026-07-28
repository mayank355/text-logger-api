from sqlalchemy.orm import Session
import models, schemas

def create_text(db: Session, text: schemas.TextCreate):
    word_count = len(text.content.split())
    db_text = models.Text(
        content=text.content,
        author=text.author,
        word_count=word_count
    )
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    return db_text

def get_all_texts(db: Session):
    return db.query(models.Text).all()

def get_text(db: Session, text_id: int):
    return db.query(models.Text).filter(models.Text.id == text_id).first()

def delete_text(db: Session, text_id: int):
    db_text = db.query(models.Text).filter(models.Text.id == text_id).first()
    if db_text:
        db.delete(db_text)
        db.commit()
    return db_text