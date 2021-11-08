FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app/app/

COPY conf/requirements.txt /mnt/
RUN pip install -Ur /mnt/requirements.txt

# https://youtrack.jetbrains.com/issue/PY-45145
# ENTRYPOINT []