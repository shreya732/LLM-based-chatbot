# Conversational Chatbot Interface with Streamlit

This project showcases a conversational chatbot built using **Streamlit**, integrated with the **Groq LLM**, **Text-to-Speech (TTS)**, and **Speech-to-Text (STT)** capabilities. The bot offers an accessible, interactive, and seamless user experience for voice and text-based interactions.

---![image](https://github.com/user-attachments/assets/6f47a652-7e5c-4584-be3d-63511fbe730e)


## Key Features

### 1. **Structured Layout**
- Leveraging Streamlit's sidebar and markdown ensures a visually intuitive and user-friendly interface.

### 2. **Customizable Interaction**
- Supports both **text input** and **speech input**, making it flexible and accessible for various users.

### 3. **Real-Time Feedback**
- Displays recognized speech for user confirmation, improving trust and accuracy.

### 4. **Concurrent Processing**
- Uses threading to run the `speak_text` function, enabling uninterrupted interaction without UI blocking.

### 5. **Secure Environment**
- API keys are stored securely in a `.env` file, minimizing risks of accidental exposure.

---
![image](https://github.com/user-attachments/assets/41f57f57-b1b1-4e85-ae34-19ae68368693)


## Workflow Overview

### **1. How Speech Input is Processed**
**Visual:** A flowchart: `Microphone > Recognizer > Text`  
**Explanation:**  
"When you speak, the bot uses a microphone to record your voice. It processes this audio using Google’s Speech Recognition service, which converts it into text that the bot can understand."

---

### **2. How the LLM Generates a Response**
**Visual:** User query traveling to a cloud, followed by a response coming back.  
**Explanation:**  
"The text query is sent to a large language model (LLM). This model, trained on vast data, uses advanced algorithms to predict and generate the most accurate response."

---

### **3. How Speech Output is Produced**
**Visual:** Response text converting into audio waves.  
**Explanation:**  
"Once the response is ready, the bot uses a text-to-speech engine to convert the text into spoken words, ensuring a natural interaction."

---![image](https://github.com/user-attachments/assets/526fa4ab-fa88-4c98-bbf4-ce0e15b518fb)


### **4. How the Bot Handles Interruptions**
**Visual:** Bot speaking with a button press to stop it.  
**Explanation:**  
"To let users interrupt, the bot stops the current text-to-speech process when a new query is detected, giving users full control of the conversation."

---

### **5. Challenges and Solutions**
**Visual:** Pop-up text showing challenges like "Speech recognition errors" and "Handling accents."  
**Explanation:**  
"Challenges include handling speech recognition errors, different accents, and noisy environments. Solutions involve using robust recognition tools and providing users the option to edit text input if needed."

---

## Closing Note
Explore the future of chatbots today! This project demonstrates how AI makes communication more interactive, accessible, and fun.  

---

## Installation and Usage

### Prerequisites
- Python 3.7+
- A `.env` file containing your API key for the Groq LLM.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/conversational-chatbot.git

