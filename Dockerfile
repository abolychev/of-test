FROM python:3
RUN useradd -d /opt/app -m app
WORKDIR /opt/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
USER app
CMD ["python3", "app.py"]
