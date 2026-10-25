from database import get_db, init_db


def create_lead(name, email, phone=None, service=None):
    with get_db() as conn:
        cursor = conn.execute(
             "INSERT INTO leads (name, email, phone, service) VALUES (?, ?, ?, ?)",
              (name, email, phone, service)
              )
        return cursor.lastrowid


    
def get_all_leads():
    with get_db()as conn:
        rows = conn.execute("SELECT * FROM  leads").fetchall()
        return [dict(row) for row in rows]


def get_lead(lead_id):
    with get_db() as conn:
        row = conn.execute(
                     "SELECT * FROM leads WHERE id = ?",
                     (lead_id,),
        ).fetchone()
        if row is None:
            return None
        return dict(row)

    

def update_lead(lead_id: int, name, email, phone, service, status):
    with get_db()as conn:
        cursor = conn.execute(
              "SELECT * FROM leads WHERE id = ?",
              (lead_id,)
              )
        lead = cursor.fetchone()

        if lead is None:
            return False 
        curr_name = name if name is not None else lead["name"]
        curr_email = email if email is not None else lead["email"]
        curr_phone = phone if phone is not None else lead["phone"]
        curr_service = service if service is not None else lead["service"]
        curr_status = status if status is not None else lead["status"]
        conn.execute("""UPDATE leads SET name = ?, email = ?, phone = ?, service = ?, status = ? 
                        WHERE id = ?""",
                        (curr_name, curr_email, curr_phone, curr_service, curr_status, lead_id),)
        return True
    

def delete_lead(lead_id):
    with get_db() as conn:
        cursor = conn.execute(
               "DELETE FROM leads WHERE id = ?",
               (lead_id,),
               )
        return cursor.rowcount > 0

    