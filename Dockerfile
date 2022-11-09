FROM python:3.10-alpine
WORKDIR /app
COPY ./requirements.txt /app/ 
RUN pip install -r requirements.txt
COPY ./app.py /app/app.py
CMD ["python", "app.py"]
