from sqlalchemy import Column, Integer, String, Text, CHAR, DECIMAL, TIMESTAMP, DATE, ForeignKey, NUMERIC
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)



class Play(Base):
    __tablename__ = "plays"
    play_id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String, nullable=False)
    duration = Column(Integer)
    genre = Column(String)
    symnost = Column(Text)

    actorplays = relationship("ActorPlay", back_populates="play")
    directorplays = relationship("DirectorPlay", back_populates="play")
    showtime = relationship("ShowTime", back_populates="play")


class Actor(Base):
    __tablename__ = "actors"
    actor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    gender = Column(CHAR)
    date_of_birth = Column(DATE)

    actorplays = relationship("ActorPlay", back_populates="actor")


class ActorPlay(Base): 
    __tablename__ = "actor_plays"
    actor_id = Column(Integer, ForeignKey("actors.actor_id"), primary_key=True)
    play_id = Column(Integer, ForeignKey("plays.play_id"), primary_key=True)

    actor = relationship("Actor", back_populates="actorplays")
    play = relationship("Play", back_populates="actorplays")



class Director(Base):
    __tablename__ = "directors"
    director_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_birth = Column(DATE)
    citizenship = Column(String) 

    directorplays = relationship("DirectorPlay", back_populates="director")


class ShowTime(Base):
    __tablename__ = "showtimes"
    date_and_time = Column(TIMESTAMP, unique=True, primary_key=True, index=True)
    play_id = Column(Integer, ForeignKey("plays.play_id"), unique=True, primary_key=True, index=True)

    play = relationship("Play", back_populates="showtime")
    tickets = relationship("Ticket", back_populates="showtime", primaryjoin="ShowTime.play_id==Ticket.play_id")
    prices = relationship("Price", back_populates="showtime", primaryjoin="ShowTime.play_id==Price.show_times_play_id")



class DirectorPlay(Base):
    __tablename__ = "director_plays"
    director_id = Column(Integer, ForeignKey("directors.director_id"), primary_key=True)
    play_id = Column(Integer, ForeignKey("plays.play_id"), primary_key=True)

    director = relationship("Director", back_populates="directorplays")
    play = relationship("Play", back_populates="directorplays")


class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    telephone_no = Column(String, nullable=False)

    tickets = relationship("Ticket", back_populates="customer",
                            primaryjoin="Customer.customer_id==Ticket.customer_customer_id")



class Seat(Base):
    __tablename__ = "seats"
    row_no = Column(Integer, unique=True, primary_key=True, index=True)
    seat_no = Column(Integer, unique=True, primary_key=True, index=True)

    tickets = relationship("Ticket", back_populates="seat", primaryjoin="Seat.seat_no==Ticket.seat_seat_no")
    prices = relationship("Price", back_populates="seat", primaryjoin="Seat.row_no==Price.seat_row_no")


class Ticket(Base):
    __tablename__ = "tickets"
    seat_row_no = Column(Integer, ForeignKey("seats.row_no"), primary_key=True)
    seat_seat_no = Column(Integer, ForeignKey("seats.seat_no"), primary_key=True)
    date_and_time = Column(TIMESTAMP, ForeignKey("showtimes.date_and_time"), primary_key=True)
    play_id = Column(Integer, ForeignKey("showtimes.play_id"), primary_key=True)
    customer_customer_id = Column(Integer, ForeignKey("customers.customer_id"), primary_key=True, index=True)
    ticket_no = Column(String, nullable=False)

    seat = relationship("Seat", back_populates="tickets", primaryjoin="Ticket.seat_seat_no==Seat.seat_no")
    showtime = relationship("ShowTime", back_populates="tickets", primaryjoin="Ticket.play_id==ShowTime.play_id")
    customer = relationship("Customer", back_populates="tickets", primaryjoin="Ticket.customer_customer_id==Customer.customer_id")


class Price(Base):
    __tablename__ = "prices"
    seat_row_no = Column(Integer, ForeignKey("seats.row_no"), primary_key=True, index=True)
    seat_seat_no = Column(Integer, ForeignKey("seats.seat_no"), primary_key=True, index=True)
    show_times_date_and_time = Column(TIMESTAMP, ForeignKey("showtimes.date_and_time"), primary_key=True)
    show_times_play_id = Column(Integer, ForeignKey("showtimes.play_id"), primary_key=True, nullable=False)
    price = Column(NUMERIC(10,2))

    seat = relationship("Seat", back_populates="prices",primaryjoin="Price.seat_seat_no==Seat.seat_no")
    showtime = relationship("ShowTime", back_populates="prices",
                             primaryjoin="Price.show_times_date_and_time==ShowTime.date_and_time")














    

