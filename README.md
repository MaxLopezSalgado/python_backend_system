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
![ss6](![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/3fae4805-9e0e-4d30-a3ba-e8b3ad761558)

### Courses Endpoint
The Rating for the entire course will be updated as per the aggregated sum of chapters as mentioned in the assignment document. 
![ss1](![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/0417a618-50b3-4267-bbd3-d5bcbff0ab51)

### Single Course Overview Endpoint
![ss2](![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/02035010-7e92-4879-b7a1-8d6ff3acfa5a)

### Chapter Details Endpoint
![ss3](![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/70112662-c495-4ba1-bfbc-db045bc51ad2)

### POST Request Endpoint to add rating to a Chapter
![ss4](![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/ca2de8da-7bda-411a-9078-6063c4b341ba)

### Success
![ss5](![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/91bb0046-b0c0-438d-9eb9-a60260f0c60f)

### Running Tests to validate all endpoints
pytest test_app.py
![ss7](![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/a6434277-9205-4370-8bb1-4838050ad56f)

### Containerizing the Application 
docker build -t my_python_app .
![ss9](![image](https://github.com/MaxLopezSalgado/python_backend_system/assets/100579900/ae7198d0-809a-4ebd-ac3a-ed2c954f9df9)
)
