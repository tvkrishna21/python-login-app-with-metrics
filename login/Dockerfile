FROM python:3.7.3-alpine3.9 as prod
RUN mkdir /app/
WORKDIR /app/
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD [ "app.py" ]
