# Gulf Bank Datathon - GenAi Track 🏆
![Gulf Bank Datathon](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/c7e0024e-5af9-44fa-8483-19275432ebf1/Website_banner/public)

## Description 🚀
Welcome to the Gulf Bank Datathon GenAi track! This competition challenges participants to leverage the power of Artificial Intelligence to solve real-world problems in the travel/flight agencies ✈️.. The final product should have an interactive chatbot that can recommend places, check flights, plan trips and possibly to book the flight. 

## Approach  📝
To solve the problem, we first built the model which has multiple component, the first one was the RAG vectorizor, which take any resource and vectorize it and make it ready to retrieve data from. The second one was Pandas Query Engine, which will take any input i.e prompt and translate it as a query to query our vector DB in first component. The last component was, API's from open sources that helps in finding real time flights and weather preditions.

## Implementation 💻
The three components were linked together by prompt enginering and by using a mapper which is a way to check the prompt scope,for example if it is related to flight booking or flight searching or weather of the country. Once it gets the scope it will capture the parameters such as origin location and destination location and it will call the matching function and pass the arguments to it.

## Result 📊
Finally, The result was not bad! we got a really good accurecy and it was responding well, but the problem was with integrating the model we built with the UI framework, which made difficulties to render the response in UI, but as a model output it was great. 🤖

## Important Notes 🎉
- There were no dataset provided.
- Very important to integrate API's to generate real data and live data. 


