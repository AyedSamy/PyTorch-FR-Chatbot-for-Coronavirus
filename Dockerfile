FROM continuumio/anaconda3:2019.10
COPY . /ayedsamy/covidchatbot
EXPOSE 5000
WORKDIR /ayedsamy/covidchatbot
RUN pip install -r requirements.txt
CMD python app.py