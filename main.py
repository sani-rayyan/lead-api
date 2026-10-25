from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from database  import init_db
from schemas import LeadCreate, LeadUpdate
from crud import create_lead, get_all_leads, get_lead, update_lead, delete_lead


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message": "Lead API is running"}


@app.post("/leads", status_code= 201)
def add_lead(lead: LeadCreate):
    id = create_lead(lead.name, lead.email, lead.phone, lead.service)
    return {"id": id, "message": "Leads saved"}


@app.get("/leads")
def get_leads():
    return get_all_leads()

@app.get("/leads/{lead_id}")
def read_lead(lead_id: int):
    lead = get_lead(lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


@app.patch("/leads/{lead_id}")
def update_lead_api(lead_id: int, lead_update: LeadUpdate):
    success = update_lead(lead_id,
                          lead_update.name,
                          lead_update.email,
                          lead_update.phone,
                          lead_update.service,
                          lead_update.status)

    if not success:
        raise HTTPException(status_code=404, detail="Not found id")
    return {"status": "success",
            "message": f"[ID: {lead_id}] Lead updated "}


@app.delete("/leads/{lead_id}")
def remove_lead(lead_id: int):
    deleted = delete_lead(lead_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Lead not found")
    return {"message": "lead deleted"}









