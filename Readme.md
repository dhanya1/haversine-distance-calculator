**Prequisite:**
1. git
2. Docker

**Instructions:**
1. git clone <repo name> 
2. cd <to_folder_with_Dockerfile>
3. docker build -t <tag_name_of_your_choice> .
4. To run unittests:\
   docker run --env-file env.txt <image_name> python -m unittest discover
5. To test the functionality:\
   docker run --env-file env.txt -p 8000:8000 <image-name>
   
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
   
   Testing the Curl way:\
   `curl -v -F distance=<distance in km as text> -F file=@localfilename 
   http:localhost:8000/distance-calculator/`
   
   
   
   
   
   
   

