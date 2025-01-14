from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import delete, select

from database import SessionDep, create_db_and_tables
from models import Coordinates


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_db_and_tables()


@app.post("/coordinates/")
def create_coordinates(coordinates: Coordinates, session: SessionDep) -> Coordinates:
    query = select(Coordinates).filter_by(lat=coordinates.lat, lon=coordinates.lon)
    result = session.exec(query).all()
    if result:
        print('Существующее значение.')
        return result[0]
    else:
        print('Запись в БД.')
        session.add(coordinates)
        session.commit()
        session.refresh(coordinates)
        return coordinates


@app.get("/coordinates/{coordinates_id}")
def read_coordinate(coordinates_id: int, session: SessionDep) -> Coordinates:
    coordinates = session.get(Coordinates, coordinates_id)
    if not coordinates:
        raise HTTPException(status_code=404, detail="coordinates not found")
    return coordinates


@app.delete("/coordinates/{coordinates_id}")
def delete_coordinates(coordinates_id: int, session: SessionDep):
    coordinates = session.get(Coordinates, coordinates_id)
    if not coordinates:
        raise HTTPException(status_code=404, detail="coordinates not found")
    session.delete(coordinates)
    session.commit()
    return {"ok": True}


@app.delete("/clear_tables")
def clear_tables(session: SessionDep):
    statement = delete(Coordinates)
    session.exec(statement)
    session.commit()
    return {"ok": True}