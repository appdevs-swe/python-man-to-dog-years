FROM python:3.8-slim-buster
WORKDIR /python-man-to-dog-years
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /python-man-to-dog-years
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]