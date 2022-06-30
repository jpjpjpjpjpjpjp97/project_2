# Documentation

1. Clone the github repository on the desired location

`git clone https://github.com/jpjpjpjpjpjpjp97/project_2.git`

2. Build the image from the command line:

`docker build -t project_2_web .`

3. Create a container with the image, with the following parameters:

`docker run -ti --rm -p 8080:8000 --name project2 project_2_web pipenv run python manage.py runserver 0.0.0.0:8000`

- You should see an output similar to this:

```text
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 30, 2022 - 03:58:23
Django version 4.0.5, using settings 'project_2.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

4. Once the test server is running, the test website should be available under http://0.0.0.0:8080/api/pokemon/ on your local machine.

5. In Mac, multiple simultaneous requests can be sent with the command:

`for i in $(seq 1 150); do curl "http://0.0.0.0:8000/api/pokemon/"; done`

6. The thread lock part of the application which writes to a file is in `project_2/pokemon/views.py` file:

```python
class PokemonViewset(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    def dispatch(self, request, *args, **kwargs):
        lock = Lock()
        Thread(target=write_to_file, args=(lock, request,)).start()
        return super().dispatch(request, *args, **kwargs)
```

7. The request's information should be written into `/project_2/api_request_login.txt` file, like the following example:

```txt
2022-06-15 05:21:01.921980 | GET | /api/pokemon/1/
2022-06-15 05:21:02.623637 | GET | /api/pokemon/1/
2022-06-15 05:21:03.073572 | GET | /api/pokemon/1/
2022-06-15 05:21:24.075804 | OPTIONS | /api/pokemon/1/
2022-06-15 05:21:25.077877 | OPTIONS | /api/pokemon/1/
2022-06-15 05:21:25.617663 | OPTIONS | /api/pokemon/1/
2022-06-15 05:21:31.836776 | GET | /api/pokemon/
2022-06-15 05:22:35.380648 | POST | /api/pokemon/
2022-06-15 05:22:37.938936 | GET | /api/pokemon/
```