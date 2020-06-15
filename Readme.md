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
   
   Now you can test the API Endpoint:\
   Base URL:
   `http://localhost:8000/`
   
   Endpoint:
   `/distance-calculator/` (Trailing / must be included)
   
   Headers:
   `Content-Type: multipart/form-data`
   
   Body:
   `file: Upload the file here`
   `distance: <distance in kilometers> (optional: Defaults to 100)`
   
   Curl command:\
   `curl -v -F distance="100" -F 
   file=@/full_path_to_current_directory/customers.txt 
   http:localhost:8000/distance-calculator/`
   
   
   
   
   
   
   

