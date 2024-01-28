FROM python:3.9
LABEL authors="<rdvid> Rafael David"
WORKDIR /fbook
COPY . .
RUN \
  pip install --upgrade pip && \
  pip install -r requirements.txt
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]