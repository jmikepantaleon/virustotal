# 📝 File Malware Scanner Challenge

## **📌 1. Requisitos previos**  

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas en tu sistema:

🔹 **Docker** (Opcional, pero recomendado)  
🔹 **Python 3.10+**  


---

## **🚀 2. Iniciar el Backend (FastAPI)**  

1️⃣ **Clona este repositorio**  
```sh
git clone git@bitbucket.org:challengepython/antivirus.git
cd antivirus
```

2️⃣ **Instala las dependencias con pip**  
```sh
pip install -r requirements.txt
```

3️⃣ **Configura la base de datos en `.env`**  
📌 **Crea un archivo `.env` dentro de `backend/` y añade:**  
```ini
SECRET_KEY=llave porporcionada por virustotal https://www.virustotal.com/

```
4️⃣ **Inicia el servidor FastAPI**  
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

📌 La API estará disponible en: **`http://localhost:8000`**  
📌 Documentación de Swagger: **`http://localhost:8000/docs`**  

---

5️⃣ **Inicia el Docker**  
```sh
docker-compose up
```

📌 La API estará disponible en: **`http://localhost`**  
📌 Documentación de Swagger: **`http://localhost/docs`**  

---

## **👨‍💻 Autor**
**Jose Miguel Pantaleon Martinez** 
