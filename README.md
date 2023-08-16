## Libraries used
```py
 contextlib
 fastapi 
 pymongo 
 bson 
 os
 dotenv  
 bson 
 pytest
```

## Endpoints

### Adding the courses.json to MongoDB using the Python script
![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/e3bd8223-6cba-475f-9a0a-7fafd60c5096)

### Courses Endpoint
The course's rating is calculated as an aggregated sum of its chapters, following the assignment document's guidelines.
![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/945cfb4e-c27a-40a1-b757-3ce1fd49e1a9)

### Single Course Overview Endpoint
![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/8723831d-e8c8-49bf-b07c-41f94d800d6f)

### Chapter Details Endpoint
![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/fcfdb476-7404-40c3-8d82-f4f8a6a384a7)

### POST Request Endpoint to Add Rating to a Chapter
![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/e508d452-78f9-478f-973c-dd45d58a5fb3)

### Success
![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/a9e3af80-b33c-45a5-bcac-96ba2635e1a0)


### Running Tests to Validate All Endpoints
To run tests: `pytest test_app.py`
![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/430ba6f4-2402-4d65-9022-1061d18a3721)

### Containerizing the Application 
To containerize: `docker build -t my_python_app .`
![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/f56cc46d-61b5-4955-99c0-6541f0d9b445)

