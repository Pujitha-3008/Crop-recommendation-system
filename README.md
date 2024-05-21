SMART CROP RECOMMENDATION SYSTEM POWERED BY MACHINE LEARNING WITH FLASK![image](https://github.com/Pujitha-3008/Crop-recommendation-system/assets/85408034/1e4884d2-5359-4da3-8c3a-c00b3d56a502)
ABSTRACT

In modern agriculture, optimizing crop selection based on various environmental and soil conditions is crucial for maximizing yield and sustainability. In this project, we propose a crop recommendation system utilizing machine learning techniques integrated with a Flask web framework. The system collects and preprocesses diverse data sources including soil type, climate, temperature, rainfall, and humidity. Through feature selection and engineering, relevant factors affecting crop growth are identified. Machine learning models, including Random Forest, are trained using the preprocessed data to predict suitable crops for a given set of conditions. Leveraging the trained models, the system then generates personalized crop recommendations tailored to the user's specific circumstances. The deployment of the system allows for widespread access, empowering farmers to make informed decisions, optimize resource utilization, and enhance agricultural productivity. Through testing, refinement, and maintenance, the system continuously evolves to adapt to changing agricultural landscapes, ensuring its relevance and effectiveness in crop selection decision-making.
![image](https://github.com/Pujitha-3008/Crop-recommendation-system/assets/85408034/7e261242-f9c4-431a-b7be-6c365b2422bd)

 INTRODUCTION

Recent advancements in data science and full stack development have transformed agriculture, particularly through crop recommendation systems. These systems leverage machine learning, data analytics, and user-friendly interfaces to offer personalized suggestions to farmers, enhancing crop selection and increasing production efficiency. With modern agriculture emphasizing the importance of judicious crop selection for optimizing yield and sustainability, data-driven strategies have become prevalent, replacing traditional methods based on experience and local knowledge. By harnessing data-driven insights, these systems support sustainable practices, minimize environmental impact, and contribute to food security and economic growth. Integration of machine learning with web technologies, such as Flask, presents a promising avenue for developing robust crop recommendation systems. This project aims to design such a system, leveraging machine learning to analyze diverse datasets and provide personalized recommendations. 
![image](https://github.com/Pujitha-3008/Crop-recommendation-system/assets/85408034/f826d34b-a725-4a0e-a153-7f3b3ce6de7d)

EXISTING SYSTEM

Crop Recommendation Systems (CRS) utilize various algorithms, including Random Forest, decision trees, SVM, KNN, ANN (including CNNs and RNNs), GBM, clustering techniques (such as K-means and hierarchical clustering), fuzzy logic systems, and ensemble methods. These algorithms analyze soil properties, climate conditions, past crop performance, and market patterns to provide tailored suggestions to farmers. Random Forest is favored for its ability to handle diverse data types and reduce overfitting, while decision trees offer simplicity and efficiency in categorization tasks. SVM is effective for classification tasks with nonlinear boundaries, while KNN groups data points based on similarity metrics. ANN, GBM, and clustering techniques are also widely used in CRS, each addressing specific needs and features of crop recommendation tasks. Additionally, ensemble methods like bagging, boosting, and stacking enhance prediction resilience and accuracy in CRS. Ongoing research and development in the field continue to introduce new algorithms and approaches to further improve CRS functionality and performance.
![image](https://github.com/Pujitha-3008/Crop-recommendation-system/assets/85408034/d3ff40d4-3edd-4d97-b160-840cf883b709)

PROPOSED SYSTEM

The proposed crop recommendation system harnesses the synergistic power of machine learning, specifically a Random Forest classifier, with a Flask backend, and a user- friendly frontend developed using HTML, CSS, and JavaScript. This system aims to revolutionize crop selection in agriculture by providing farmers with actionable insights derived from comprehensive datasets encompassing soil attributes, climate conditions, and historical crop performance. Through intuitive user interfaces, farmers can effortlessly input geographical data, soil characteristics, and climatic conditions, while dynamic JavaScript-driven features enhance interactivity and responsiveness. The Flask backend orchestrates seamless communication between user inputs and the machine learning model, facilitating the generation of personalized crop recommendations tailored to each user's specific needs. By integrating cutting-edge technologies and fostering data-driven decision-making, the proposed system endeavours to empower farmers, optimize resource utilization, and ultimately drive sustainable agricultural practices forward.
![image](https://github.com/Pujitha-3008/Crop-recommendation-system/assets/85408034/464740a9-ffba-48cb-ba13-9cb2caa713f2)

HARDWARE AND SOFTWARE REQUIREMENTS
SYSTEM REQUIREMENTS TECHNOLOGIES USED:
MACHINE LEARNING MODELS USED: Random Forest
Flask framework for integration of frontend and backend
JavaScript frame work with CSS and HTML for front end
SOFTWARE REQUIREMENTS:
Operating System: Windows 7 or 10 Ultimate, Linux, Mac.
Coding Language: React Js, Node Js for Front-end and Express Js for Back-end 
Software Environment: Visual Studio Code 
Database: MongoDB
HARDWARE REQUIREMENTS:
Processor: Intel 1-3, 5, to 7 RAM: 4GB 
RAM or higher 
Hard Disk: 500GB or higher
MODULES
HTML: HTML structures and presents content in crop recommendation websites, creating layouts, organizing elements, and incorporating interactive forms for personalized recommendations. It serves as the foundation for intuitive and user-friendly interfaces, facilitating access to valuable agricultural insights.
CSS: CSS styles HTML elements for visual appeal and cohesion, defining color schemes, typography, layout, and responsiveness. It incorporates animations and transitions for interactive feedback, enhancing the user experience of the crop recommendation system website.
JavaScript: JavaScript enhances user interaction in the frontend, enabling dynamic features for inputting data. Integration with Flask backend facilitates real-time generation of personalized crop recommendations, empowering farmers with actionable insights.
Flask API: Flask API handles communication between frontend and backend for crop recommendations. It creates RESTful APIs for receiving input parameters and passes them to the machine learning model for tailored recommendations.
Mongo DB: MongoDB manages contact page functionality in the crop recommendation system, facilitating efficient storage and retrieval of user contact information. Its flexible document-oriented model accommodates diverse data types, ensuring scalability and responsiveness for enhanced user engagement.
![image](https://github.com/Pujitha-3008/Crop-recommendation-system/assets/85408034/8e611a25-943c-4eb2-8354-6a3a5b38b2f2)

METHOD
Algorithm Used
Random Forest: The machine learning flow begins with the collection of diverse agricultural data, including soil type, climate conditions, historical crop yields, and agricultural practices. This data is then preprocessed to handle missing values, normalize features, and encode categorical variables. Subsequently, the preprocessed data is divided into training and testing sets for model evaluation. The Random Forest algorithm is then applied to the training data, where multiple decision trees are trained on different subsets of the dataset using random feature selection. During the training process, each decision tree learns to classify crops based on the provided features, such as soil characteristics and climate attributes. By leveraging the collective knowledge of multiple decision trees, Random Forest can effectively capture complex interactions between different variables, resulting in more reliable recommendations compared to traditional single-tree methods. Furthermore, Random Forest is resilient to overfitting and performs well with large datasets, making it suitable for handling the diverse and voluminous agricultural data often encountered in crop recommendation systems. Finally, the trained model is deployed into the crop recommendation system, where it assists farmers and agricultural stakeholders in making informed decisions to optimize crop productivity and yield. Overall, the integration of the Random Forest classifier algorithm into a crop recommendation system significantly improves the precision and accuracy of crop recommendations, thereby facilitating sustainable agricultural practices and enhancing overall crop yield.
![image](https://github.com/Pujitha-3008/Crop-recommendation-system/assets/85408034/19c9f01b-c54b-4971-b31e-33684fd9617b)
# Login page
![alt text](https://github.com/kritimyantra/flask-authentication-system/blob/main/login.png?raw=true)
# Register page
![alt text](https://github.com/kritimyantra/flask-authentication-system/blob/main/register.png?raw=true)
# Dashboard page
![alt text](https://github.com/kritimyantra/flask-authentication-system/blob/main/dashboard.png?raw=true)
