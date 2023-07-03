FROM python:3.9-slim-bullseye

# RUN apt-get update && apt-get install -y openjdk-11-jdk && apt-get install -y ant && apt-get clean; 

WORKDIR /app
COPY requirements.txt requirements.txt

COPY . /app
# RUN python codes/start_solr.py 
# CMD ["python", "codes/start_solr.py"]

RUN pip install -r requirements.txt
# COPY . /app

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
# RUN python codes/start_solr.py 
ENTRYPOINT ["streamlit", "run", "codes/search_engine.py", "--server.port=8501", "--server.address=0.0.0.0"]