
FROM jpjpjpjpjpjpjp97/project_2:latest

WORKDIR /project_2
ADD ./project_2 /project_2/
COPY Pipfile /project_2/
RUN pip install pipenv && pipenv install
EXPOSE 8000