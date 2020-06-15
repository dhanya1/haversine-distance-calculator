**Introduction**

The Haversine distance calculation code is wrapped into an API using Flask 
and containerized with Docker.

**Features**\
The endpoint allows you to upload a file and optionally specify a range 
within which the customer must be to get an invite. The range defaults to 100.

You can configure a different branch/office location as the origin by updating 
co-ordinates in the env_file, or run multiple versions of the code by running
 containers with different env files.


**Prequisite:**
1. git
2. Docker

**Instructions:**
1. git clone <repo name> 
2. cd <to_folder_with_Dockerfile>
3. `docker build -t haversine .`
4. To run unittests:\
   `docker run --env-file env.txt haversine:latest python -m unittest 
   discover`
5. To test the functionality:\
   `docker run --env-file env.txt -p 8000:8000 haversine:latest`
   
   To test the API Endpoint (Postman or similar):\
   Base URL:
   `http://localhost:8000/`
   
   Endpoint:
   `/distance-calculator/` (Trailing / must be included)
   
   Headers:
   `Content-Type: multipart/form-data`
   
   Body (formdata):
   `(keyword: file, type:file) : Upload the file here`
   `(keyword:distance, type:text): <distance in kilometers> (optional: Defaults
    to 100)`
   
   Curl command:\
   `curl -v -F distance="100" -F 
   file=@/full_path_to_current_directory/customers.txt 
   http://localhost:8000/distance-calculator/`
   
   
   
   
   
   
   

