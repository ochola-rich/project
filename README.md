# Smart Farming App  

**Empowering farmers with AI-driven insights and sustainable practices**  

---

## **Overview**  
The Smart Farming App is a revolutionary platform that combines advanced AI technologies and user-friendly tools to enhance farming practices. By leveraging OpenAI's Gemini model, farmers receive personalized recommendations, timely weather updates, and diagnostics based on media uploads. The goal is to improve agricultural productivity, reduce losses, and promote sustainability.  

---

## **Key Features**  
1. **AI Recommendations**:  
   - Diagnose farming issues and suggest actionable solutions.  
   - Provide crop management tips tailored to local conditions.  

2. **Weather Integration**:  
   - Display real-time weather updates and forecasts to aid farm planning.  

3. **Media Uploads**:  
   - Farmers can upload images or videos for AI-powered analysis of crop health and other issues.  

4. **Farm Management Tools**:  
   - Add and manage farm profiles, including crop details and field characteristics.  

5. **Notification System**:  
   - Alert farmers about critical updates, recommendations, and potential risks.  

---

## **Technologies Used**  
- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, and Django Template Language  
- **AI**: OpenAI Gemini Model Integration  
- **Database**: SQLite (for prototyping)  
- **APIs**: OpenWeatherMap API for weather data  

---

## **How It Works**  
1. **Farm Setup**: Farmers can create profiles for their farms with essential details.  
2. **AI Diagnosis**: Upload photos or videos of crops, and the AI provides insights into issues like pest infestations or nutrient deficiencies.  
3. **Weather Alerts**: View weather updates and how they might impact farming activities.  
4. **Actionable Notifications**: Get timely alerts for fertilization, irrigation, or harvest based on AI and weather data.  

---

## **Installation Instructions**  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/yourusername/smart-farming-app.git  
   cd smart-farming-app  
   ```  

2. **Set Up Virtual Environment**:  
   ```bash  
   python3 -m venv env  
   source env/bin/activate  
   ```  

3. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set Environment Variables**:  
   - Create a `.env` file in the root directory with the following keys:  
     ```
     OPENAI_API_KEY=<your_openai_api_key>
     WEATHER_API_KEY=<your_openweathermap_api_key>
     ```  

5. **Run Migrations**:  
   ```bash  
   python manage.py makemigrations  
   python manage.py migrate  
   ```  

6. **Start the Development Server**:  
   ```bash  
   python manage.py runserver  
   ```  

---

## **Usage**  
1. Navigate to `http://127.0.0.1:8000/` in your browser.  
2. Register or log in to access the platform.  
3. Explore features such as adding farms, uploading media, and checking AI recommendations.  

---

## **Future Enhancements**  
- Expand crop recommendations for different regions.  
- Integrate support for IoT sensors to collect real-time farm data.  
- Provide financial insights, such as cost optimization and ROI analysis.  

---

## **Contributions**  
Contributions are welcome! Please submit issues or pull requests via the GitHub repository.  

---

## **License**  
This project is licensed under the gnu lincence.  

---

For more information, feel free to contact us at **[email](richardochola3@gmail.com)**.
