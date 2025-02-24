import urllib
from fastapi import FastAPI, File, UploadFile,HTTPException, Depends
from .auth.authentication import oauth2_scheme, get_current_user, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from .models.user import User
from .data.users import users_db
import requests
from .config import settings
app = FastAPI()


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if user is None or user.password != form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/files/")
async def create_file(file: UploadFile, username: str = Depends(get_current_user)):
    content = await file.read()
    files = {"file": content}
    url = "https://www.virustotal.com/api/v3/files"

    headers = {
        "accept": "application/json",
        "X-Apikey": settings.SECRET_KEY
    }
    response = requests.post(
                url,
                files=files,
                headers=headers,

            )

    if response.status_code == 200:
        data= response.json()

        id = urllib.parse.quote_plus(data['data']['id'])
        url=f"https://www.virustotal.com/api/v3/analyses/{id}"

        report = requests.get(url, headers=headers)


        return report.json()
    raise HTTPException(status_code=400, detail=f"No se acepto la conexion {username}")
