FROM python:3

WORKDIR /webapp
COPY . /webapp

RUN pip install flask
RUN pip install ibm_watson
RUN pip install flask_cors
RUN pip install PILLOW
RUN pip install pyopenssl


EXPOSE 4000

CMD ["python", "app.py"]
