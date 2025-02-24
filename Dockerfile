FROM python:3.13 
 
RUN mkdir /app
 
WORKDIR /app
 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
RUN pip install --upgrade pip 
 

COPY requirements.txt  /app/

RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app/
 

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]