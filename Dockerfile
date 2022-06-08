
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project_2
ADD ./project_2 /project_2/
COPY Pipfile /project_2/
RUN pip install pipenv && pipenv install
EXPOSE 8000