This is an assistant Chatbot that can help women be aware of the breast cancer, as Pink October is breast cancer awareness month.

<h1>📁Files: </h1>  <br />
🔸data/nlu.yml : NLU training data stores structured information about user messages.  <br />
🔸data/stories.yml : Stories are a type of training data used to train your assistant's dialogue management model. Stories can be used to train models that are able to generalize to unseen conversation paths.  <br />
🔸domain.yml : The domain defines the universe in which your assistant operates.  <br />
🔸config.yml : training configurations for the NLU pipeline and policy ensemble


<h1>👩‍🔧Create a new environment: </h1>  <br />

🔸 create a new environment using the following commands (the environment name is rasa_env): <br />
conda create --name rasa_env <br />
🔸 activate the new environment: <br />
conda activate rasa_env <br />
🔸 install json: <br />
conda install json <br />
🔸 install tensorflow: <br />
conda install tensorflow <br />
🔸 install rasa: <br />
conda install rasa <br />
🔸 install yaml: <br />
conda install yaml <br />
🔸 install flask: <br />
conda install flask <br />
🔸 install responses: <br />
conda install responses <br />
🔸 install transformers: <br />
conda install transformers <br />
<br />

<h1>🤖 Run the Bot: </h1>  <br /> 
🔸 Use rasa train to train a model. <br /> 
Then: <br /> 
🔸 rasa run actions  <br /> 
run the following command to run rasa server : <br /> 
🔸 rasa run --endpoints endpoints.yml --port 5005 --credentials credentials.yml --cors "*" <br />
run the following command to run the flask application:  <br /> 
🔸 python web_app.py

<h1>🤖 Test the Bot: </h1>  <br /> 
To validate your data and stories run the following command: <br /> 
🔸 rasa data validate <br /> 
To run your test stories: <br /> 
🔸 rasa test <br /> 
To test the NLU model separately start by splitting your NLU data into train and test sets using:  <br /> 
🔸 rasa data split nlu  <br /> 
then: <br /> 
🔸 rasa test nlu --nlu train_test_split /test_data.yml
