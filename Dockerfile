FROM python:3.14.2

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "analytics.py", "--server.address=0.0.0.0"]