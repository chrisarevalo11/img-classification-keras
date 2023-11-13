FROM tensorflow/tensorflow:latest

WORKDIR /app

COPY . /app

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN pip install waitress

EXPOSE 8000

CMD ["waitress-serve", "--port=8000", "app.app:app"]

