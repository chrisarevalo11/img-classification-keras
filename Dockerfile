FROM tensorflow/tensorflow:latest

WORKDIR /app

COPY . /app

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
