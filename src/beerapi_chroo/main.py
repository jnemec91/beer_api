import logging
from beerminer_chroo.beer import Beer
from beerminer_chroo.database import Database
from fastapi import FastAPI

app = FastAPI()
database = Database("beers.db")

logging.basicConfig(level=logging.INFO)
logging.info("Starting Beer API")


@app.get("/beers/fuzzy/{beer_name}/")
async def beers_fuzzy(beer_name: str):
    logging.info(f"Searching for beers with name {beer_name}")
    beers = database.find_fuzzy(Beer(beer_name))
    logging.info(f"Found {len(beers)} beers")
    
    return {"response": beers}

@app.get("/beers/exact/{beer_name}/")
async def beers_exact(beer_name: str):
    logging.info(f"Searching for beers with name {beer_name}")
    beers = database.find_exact(Beer(beer_name))
    logging.info(f"Found {len(beers)} beers")
    
    return {"response": beers}