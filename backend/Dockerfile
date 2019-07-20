FROM python:3

WORKDIR /backend
COPY . backend

RUN pip install flask
RUN pip install ibm_watson

EXPOSE 5000

CMD ["python", "backend/app.py"]
