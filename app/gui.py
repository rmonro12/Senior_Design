# This Python code is for the GUI to interact with the ViewSonic LS740HD commands.

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .serial_comm import ProjectorSerial
from .controller import ProjectorController

app = FastAPI()
template = Jinja2Templates(directory="templates")

# --- Initialize hardware once ---
serial_iface = ProjectorSerial(port="COM3")  # change as needed
projector = ProjectorController(serial_iface)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post("/power/on")
def power_on():
    projector.power_on()
    return {"status": "Power ON command sent"}

@app.post("/power/off")
def power_off():
    projector.power_off()
    return {"status": "Power OFF command sent"}

@app.on_event("shutdown")
def shutdown_event():
    print("Closing serial connection...")
    serial_iface.close()