##Weather Buddy 🌤️ 
Weather Buddy is a user-friendly Django-based weather application that allows users to check real-time weather conditions for any city worldwide. 
🌎 Designed with a visually appealing interface, the application provides detailed information like:

🌡️ Current Temperature
📉 Minimum and 📈 Maximum Temperatures
🌬️ Wind Speed
🕒 Last Updated Time


#Getting Started 🚀
1/Create a Virtual Environment
Navigate to the project directory and create a virtual environment.

![image](https://github.com/user-attachments/assets/3084a438-44a2-4fe2-89af-0479d02af57d)

2/Activate the Virtual Environment
Activate the virtual environment to isolate project dependencies

![image](https://github.com/user-attachments/assets/1a5aa597-e914-4fd9-b397-1e7dc422f446)

3/Install the Requirements
The project includes a requirements.txt file. Use the following command to install all necessary dependencies:


![image](https://github.com/user-attachments/assets/61fe3107-4d55-4bf9-a347-e438aa5531bc)

Optional: Freeze the installed packages into the requirements.txt file if you make changes:


![image](https://github.com/user-attachments/assets/da7074f5-79d5-4f6b-b24c-ce5f00a77efc)


4/Run the Django Server
Start the development server to view your project in a browser:

![image](https://github.com/user-attachments/assets/1a572f5d-7f93-492b-9c45-b9a9c3868485)

#Security Notes 🔐
1/ How to Generate a Secure Key?
in your terminal : 
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
-->This will output a secure, random string similar to:
" &68%$r7+=m1+pynwhd22=sm8x6v3u)i9+98j7wg@&g+w4=-1vv "

2/To Set Environment Variables for Production 

![image](https://github.com/user-attachments/assets/32439387-10be-4d44-87ed-530d5090f92b)

#API Integration: OpenWeatherMap
This project uses the OpenWeatherMap API to fetch real-time weather data for cities worldwide. The data includes details such as current temperature, minimum and maximum temperatures, wind speed, and the last updated time.

API Endpoint
The weather data is retrieved using the following endpoint:


--> https://api.openweathermap.org/data/2.5/weather
API Parameters
To fetch weather data, the API requires the following parameters:

q: The name of the city (e.g., q=Mumbai).
appid: Your unique API key for authentication.
units (Optional): The units of measurement (e.g., units=metric for Celsius).


#Application Workflow 🌟
# 🏠 Homepage Features
🔍 Search Field: Users can input the city's name to get its weather information.
🎨 Interactive Design: A beautiful cloud-themed background and minimalistic layout ensure an engaging user experience.
📋 Weather Details: Displayed in an organized card format for better readability.
Homepage: The application greets users with a search bar where they can enter a city name. Upon clicking the search icon, the app fetches real-time weather data for the selected city.

![image](https://github.com/user-attachments/assets/5838daf3-a964-41cd-bd24-efc88714671b)
![image](https://github.com/user-attachments/assets/852f6ab0-a9ec-446d-8930-b0d8c73d1c2d)


City Search Results: The weather details are displayed once the user enters a city name and it mentions the country in the display as well . 

🌟 Information includes:

🌡️ Current Temperature
📉 Minimum Temperature
📈 Maximum Temperature
🌬️ Wind Speed
🕒 Last Updated Time


🌍 Example Cities
* My beautiful city Sousse 🌴
  
  ![image](https://github.com/user-attachments/assets/c49443cb-71d1-4407-bc93-9114934adf4f)

* Paris 🗼

  ![image](https://github.com/user-attachments/assets/59a575fa-ad3c-408d-9bba-d18d78d366e6)

* Padova 🇮🇹
  
  ![image](https://github.com/user-attachments/assets/8f2f8ecb-59c2-4d0a-8589-85bf5fa13a79)

*Mumbai 

![image](https://github.com/user-attachments/assets/178b1d34-e647-4f68-877d-c8dc97aa2148)

*Bali 

![image](https://github.com/user-attachments/assets/40562892-b0b3-453b-8e2a-6d5947a323c4)



🔑 Features Recap
✅ Responsive Design: Ensures compatibility across various devices.
✅ Accurate Weather Data: Utilizes reliable APIs for real-time updates.
✅ User-Friendly Interface: Intuitive design with clear instructions.
✅ Secure and Scalable: Uses Django’s robust framework for scalability and security.

# Conclusion
---> Weather Buddy simplifies the process of checking weather updates with an aesthetically pleasing design and efficient backend architecture. It's a perfect tool for users who want to "Know Before You Go."
