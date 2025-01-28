# weather

##Create a Virtual Environment
Navigate to the  project directory and create a virtual environment.


![image](https://github.com/user-attachments/assets/3084a438-44a2-4fe2-89af-0479d02af57d)

##Activate the Virtual Environment


![image](https://github.com/user-attachments/assets/1a5aa597-e914-4fd9-b397-1e7dc422f446)

## Install the Requirements
The project has a requirements.txt file, you can install the necessary packages by running it : 


![image](https://github.com/user-attachments/assets/61fe3107-4d55-4bf9-a347-e438aa5531bc)

PS : Freeze Installed Packages into the  requirements.txt


![image](https://github.com/user-attachments/assets/da7074f5-79d5-4f6b-b24c-ce5f00a77efc)

##Run the Django Server
Start the development server to view the  project:


![image](https://github.com/user-attachments/assets/1a572f5d-7f93-492b-9c45-b9a9c3868485)



PS : 
1/ How to Generate a Secure Key?
in your terminal : 
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
-->This will output a secure, random string similar to:
" &68%$r7+=m1+pynwhd22=sm8x6v3u)i9+98j7wg@&g+w4=-1vv "

2/To Set Environment Variables for Production 

![image](https://github.com/user-attachments/assets/32439387-10be-4d44-87ed-530d5090f92b)
