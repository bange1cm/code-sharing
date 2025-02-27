import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from web import circle
from data.init import conn


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks, such as loading a bunch of stuff
	print("Starting up!")
	yield
    # Shutdown, such as closing open files etc
	# Commit changes and gracefully close
	print("Closing what was opened!")
	conn.commit()
	conn.close()



app = FastAPI(lifespan=lifespan)

app.include_router(circle.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)