from pydantic import BaseModel
from datetime import datetime, date

class PlayBase(BaseModel):
    title : str
    duration : int
    genre : str
    symnost : str

class ActorBase(BaseModel):
    actor_id : int
    name : str
    gender : str
    date_of_birth : date

class ActorPlayBase(BaseModel): 
    actor_id : int
    play_id : int

class DirectorBase(BaseModel):
    director_id : int
    name : str
    date_of_birth : date
    citizenship : str

class ShowTimeBase(BaseModel):
    date_and_time : datetime
    play_id : int

class DirectorPlayBase(BaseModel):
    director_id : int
    play_id : int

class CustomerBase(BaseModel):
    customer_id : int
    name : str
    telephone_no : str

class SeatBase(BaseModel):
    row_no : int
    seat_no : int

class TicketBase(BaseModel):
    seat_row_no : int
    seat_seat_no : int
    date_and_time : datetime
    play_id : int
    customer_customer_id : int
    ticket_no : str

class PriceBase(BaseModel):
    seat_row_no : int
    seat_seat_no : int
    show_times_date_and_time : datetime
    show_times_play_id : int
    price  : float







