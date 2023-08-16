## Libraries used
```py
 contextlib
 fastapi 
 pymongo 
 bson 
 os
 dotenv 
 pymongo 
 bson 
 pytest
```

## Endpoints

### Adding the courses.json to MongoDB using the Python script
![Image](https://github.com/MaxLopezSalgado/python_backend_system/blob/main/assets/100579900/3fae4805-9e0e-4d30-a3ba-e8b3ad761558.png)

### Courses Endpoint
The course's rating is calculated as an aggregated sum of its chapters, following the assignment document's guidelines.
![Image](https://github.com/MaxLopezSalgado/python_backend_system/blob/main/assets/100579900/0417a618-50b3-4267-bbd3-d5bcbff0ab51.png)

### Single Course Overview Endpoint
![Image](https://github.com/MaxLopezSalgado/python_backend_system/blob/main/assets/100579900/02035010-7e92-4879-b7a1-8d6ff3acfa5a.png)

### Chapter Details Endpoint
![Image](https://github.com/MaxLopezSalgado/python_backend_system/blob/main/assets/100579900/70112662-c495-4ba1-bfbc-db045bc51ad2.png)

### POST Request Endpoint to Add Rating to a Chapter
![Image](https://github.com/MaxLopezSalgado/python_backend_system/blob/main/assets/100579900/ca2de8da-7bda-411a-9078-6063c4b341ba.png)

### Success
![Image](https://github.com/MaxLopezSalgado/python_backend_system/blob/main/assets/100579900/91bb0046-b0c0-438d-9eb9-a60260f0c60f.png)

### Running Tests to Validate All Endpoints
To run tests: `pytest test_app.py`
![Image](https://github.com/MaxLopezSalgado/python_backend_system/blob/main/assets/100579900/a6434277-9205-4370-8bb1-4838050ad56f.png)

### Containerizing the Application 
To containerize: `docker build -t my_python_app .`
![Image](https://github.com/MaxLopezSalgado/python_backend_system/blob/main/assets/100579900/ae7198d0-809a-4ebd-ac3a-ed2c954f9df9.png)
