import os
import uvicorn
from fastapi import FastAPI, Form, HTTPException

app = FastAPI(title="QuMail Identity Registry")
USER_REGISTRY = {}

# Inside identity_server.py
@app.post("/register")
async def register(email: str = Form(...), level3_pk: str = Form(...), level4_pk: str = Form(...)):
    # This automatically overwrites the old dictionary entry for this email
    USER_REGISTRY[email] = {
        "3": level3_pk,
        "4": level4_pk
    }
    return {"status": "success", "detail": f"Keys rotated for {email}"}

@app.get("/lookup/{email}")
async def lookup(email: str):
    if email not in USER_REGISTRY:
        raise HTTPException(status_code=404, detail="User not found")
    return USER_REGISTRY[email]

if __name__ == "__main__":
    # Render provides the PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)