# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app/


ENV PYTHONPATH "${PYTHONPATH}:/code/app/"

# 
ENTRYPOINT uvicorn --host 0.0.0.0 app.main:app --reload
