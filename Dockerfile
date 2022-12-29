FROM python:3.8-slim
WORKDIR usr/app/
COPY . /usr/app/
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]