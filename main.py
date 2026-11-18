from fastapi import FastAPI    
from product import schemas
from database import engine, SessionLocal
from product import models
from fastapi.params import Depends
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  

@app.post('/products')
def add(request:schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description, price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get('/products')
def all_products(db:Session=Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get('/products/{id}')
def product(id,db:Session=Depends(get_db)):
   product = db.query(models.Product).filter(models.Product.id==id).first()
   return product

@app.delete('/products/{id}')
def delete(id, db:Session=Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False )
    db.commit()
    return{'message':'product is deleted'}


