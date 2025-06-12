from fastapi import FastAPI, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import Play, Actor, Director, Ticket, Customer, ShowTime
from schema import PlayBase, ActorBase, DirectorBase, TicketBase, CustomerBase, ShowTimeBase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/plays/")
async def get_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    post = db.query(Play).offset(skip).limit(limit).all()
    return post

@app.post("/plays/", response_model=PlayBase)
async def create_play(play:PlayBase, db: Session = Depends(get_db)):
    new_play = Play(**play.model_dump())
    db.add(new_play)
    db.commit()
    db.refresh(new_play)
    return new_play 

@app.put("/plays/{play_id}")
async def update_play(play_id: int, updated: PlayBase, db: Session = Depends(get_db)):
    play = db.query(Play).filter(Play.play_id==play_id).first()

    if not play:
        raise HTTPException(status_code=404, detail="play not found")
    for key, value in updated.model_dump().items(): 
        setattr(play, key, value)
    db.commit()
    db.refresh(play)
    return updated

@app.delete("/plays/{play_id}")
async def delete_play(play_id: int, db: Session = Depends(get_db)):
    play = db.query(Play).filter(Play.play_id==play_id).first()

    if not play:
        raise HTTPException(status_code=404, detail="play not found")
    db.delete(play)   
    db.commit()
    return {f"Play with {play_id} deleted"}


@app.get("/actors/")
async def get_actor(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    actor = db.query(Actor).offset(skip).limit(limit).all()
    return actor


@app.post("/actors/")
async def create_actor(actor: ActorBase, db: Session = Depends(get_db)):
    new_actor = Actor(**actor.model_dump())
    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)
    return new_actor

@app.put("/actors/{actor_id}")
async def update_actor(actor_id: int, updated: ActorBase, db: Session = Depends(get_db)):
    actor = db.query(Actor).filter(Actor.actor_id == actor_id).first()

    if not actor:
        raise HTTPException(status_code=404, detail="actor not found")
    for key, value in updated.model_dump().items():
        setattr(actor, key, value)
    db.commit()
    db.refresh(actor)
    return updated

@app.delete("/actors/{actor_id}")
async def delete_actor(actor_id: int, updated: ActorBase, db: Session = Depends(get_db)):
    actor = db.query(Actor).filter(Actor.actor_id == actor_id).first()

    if not actor:
        raise HTTPException(status_code=404, detail="actor not found")
    db.delete(actor)
    db.commit()
    return {"Message": "Actor Deleted"}


@app.get("/directors/")
async def get_director(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    director = db.query(Director).offset(skip).limit(limit).all()
    return director


@app.post("/directors/")
async def create_director(director: DirectorBase, db: Session = Depends(get_db)):
    new_director = Director(**director.model_dump())
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    return new_director

@app.put("/directors/{director_id}")
async def update_director(director_id: int, updated: DirectorBase, db: Session = Depends(get_db)):
    director = db.query(Director).filter(Director.director_id == director_id).first()

    if not director:
        HTTPException(status_code=404, detail="director not found")
    for key, value in updated.model_dump().items():
        setattr(director, key, value)
    db.commit()
    db.refresh(director)
    return updated


@app.delete("/directors/{director_id}")
async def delete_director(director_id: int, updated: DirectorBase, db: Session = Depends(get_db)):
    director = db.query(Director).filter(Director.director_id == director_id).first()

    if not director:
        HTTPException(status_code=404, detail="director not found")
    for key, value in updated.model_dump().items():
        setattr(director, key, value)
    db.commit()
    db.refresh(director)
    return updated


@app.get("/tickets/")
async def get_ticket(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).offset(skip).limit(limit).all()
    return ticket

@app.post("/tickets/")
async def generate_ticket(ticket: TicketBase, db: Session = Depends(get_db)):
    new_ticket = Ticket(**ticket.model_dump())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@app.put("/tickets/{customer_customer_id}")
async def update_ticket(customer_customer_id: int, updated: TicketBase, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.customer_customer_id == customer_customer_id).first()

    if not ticket:
        HTTPException(status_code=404, detail="ticket not found")
    for key, value in updated.model_dump().items():
        setattr(ticket, key, value)
    db.commit()
    db.refresh(ticket)
    return updated

@app.delete("/tickets/{customer_customer_id}")
async def delete_ticket(customer_customer_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.customer_customer_id == customer_customer_id).first()

    if not ticket:
        HTTPException(status_code=404, detail="ticket not found")
    db.delete(ticket)
    db.commit()
    return {"Message": "Deleted Successfully"}



@app.get("/customers/")
async def get_customer(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    customer = db.query(Customer).offset(skip).limit(limit).all()
    return customer

@app.post("/customers/")
async def generate_customer(customer: CustomerBase, db: Session = Depends(get_db)):
    new_customer = Customer(**customer.model_dump())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@app.put("/customers/{customer_id}")
async def update_customer(customer_id: int, updated: TicketBase, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()

    if not customer:
        HTTPException(status_code=404, detail="customer not found")
    for key, value in updated.model_dump().items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer) 
    return updated

@app.delete("/customers/{customer_id}")
async def update_customer(customer_id: int,  db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()

    if not customer:
        HTTPException(status_code=404, detail="customer not found")
    db.delete(customer)
    db.commit()
    return {"Message": "Deleted Successfully"}


@app.get("/showtimes/")
async def get_showtime(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    showtime = db.query(ShowTime).offset(skip).limit(limit).all()
    return showtime

@app.post("/showtimes/")
async def generte_showtime(showtime: ShowTimeBase, db: Session = Depends(get_db)):
    new_showtime = ShowTime(**showtime.model_dump())
    db.add(new_showtime)
    db.commit()
    db.refresh(new_showtime)
    return new_showtime


@app.put("/showtimes/{play_id}")
async def update_showtimes(play_id: int, updated: ShowTimeBase, db: Session = Depends(get_db)):
    showtime = db.query(ShowTime).filter(ShowTime.play_id == play_id).first() 

    if not showtime:
        HTTPException(status_code=404, detail="showtime not found")
    for key, value in updated.model_dump().items():
        setattr(showtime, key, value)
    db.commit()
    db.refresh(showtime) 
    return updated

@app.delete("/showtimes/{play_id}")
async def delete_showtimes(play_id: int, db: Session = Depends(get_db)):
    showtime = db.query(ShowTime).filter(ShowTime.play_id == play_id).first() 

    if not showtime:
        HTTPException(status_code=404, detail="showtime not found")
    db.delete(showtime)
    db.commit()
    return {"Message": "Deleted Successfully"}


    