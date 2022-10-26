FROM python:3.10.6

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "streamlit", "run", "data.py", "--server.port=8501", "server.address=0.0.0.0" ]