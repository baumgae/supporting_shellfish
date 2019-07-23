FROM python:3

WORKDIR /backend
COPY . /backend

RUN pip install flask
RUN pip install ibm_watson
RUN pip install flask_cors
RUN pip install PILLOW


EXPOSE 4000

CMD ["python", "app.py"]
