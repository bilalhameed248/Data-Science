"""
Importing Required Libraries
"""

import os
import datetime 
import pandas as pd 
from datasets import load_dataset
from transformers import BertTokenizer
from transformers import AutoTokenizer, AutoModel
from transformers import AutoModelForSequenceClassification
import numpy as np
from datasets import load_metric
from transformers import TrainingArguments, Trainer
from transformers import pipeline

# Get Current working directory
my_dir = os.getcwd() + '/' 

"""
Load dataset using load_dataset function from datasets class
"""
dataset = load_dataset('csv', data_files={'train': './train_new.csv', 'test': './test_new.csv'})

"""
Before we can feed those texts to our model, we need to preprocess them. 
This is done by a Transformers Tokenizer which will (as the name indicates) 
tokenize the inputs (including converting the tokens to their corresponding 
IDs in the pretrained vocabulary) and put it in a format the model expects, 
as well as generate the other inputs that model requires.
To do all of this, we instantiate our tokenizer with the AutoTokenizer.from_pretrained
method, which will ensure:
"""
tokenizer = AutoTokenizer.from_pretrained('dmis-lab/biobert-v1.1')

"""
Saving The Tokenizer
"""
tokenizer.save_pretrained(my_dir+"save_tokenizer")
"""
Loading Tokenizer From Save Directory
"""
tokenizer = AutoTokenizer.from_pretrained('./save_tokenizer/')

"""
We can then write the function that will preprocess our samples. 
We just feed them to the tokenizer with the argument truncation=True. 
This will ensure that an input longer that what the model selected can
handle will be truncated to the maximum length accepted by the model.
"""
def tokenize_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True)

"""
To apply this function on all the pairs of sentences in our dataset, 
we just use the map method of our dataset object we created earlier. 
This will apply the function on all the elements of all the splits in 
dataset, so our training and testing data will be preprocessed in one 
single command
"""
tokenized_datasets = dataset.map(tokenize_function, batched=True)


small_train_dataset = tokenized_datasets['train']
small_eval_dataset = tokenized_datasets['test']

"""
Now that our data is ready, we can download the pretrained model and fine-tune it. 
Since our task is of the text classification kind, we use the AutoModelForSequenceClassification 
class. Like with the tokenizer, the from_pretrained method will download and cache the model for us.
"""
model = AutoModelForSequenceClassification.from_pretrained("dmis-lab/biobert-v1.1", num_labels=2)

"""
Save The Downloaded Model
"""
model.save_pretrained(my_dir+"save_model")

"""
Load Model from save Directory
"""
model = AutoModelForSequenceClassification.from_pretrained("./save_model/", num_labels=2)

# Defining Metric
metric = load_metric("accuracy")


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

"""
TrainingArguments, which is a class that contains all the attributes to
customize the training. It requires one folder name, which will be used 
to save the checkpoints of the model, and all other arguments are optional:
"""
training_args = TrainingArguments(
         overwrite_output_dir = 'True',
         output_dir="./test_trainer/",
         evaluation_strategy="epoch",
         num_train_epochs=12, 
         save_total_limit = 2,
         save_strategy = "no",
         load_best_model_at_end=False)


"""
Then we just need to pass all of this along with our datasets to the Trainer:
"""

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics,
)

print("\n\nTraning Start\n\n")

trainer.train()

print("Saving the Fine Tuned model")

trainer.save_model()

"""
Calling Prediction On small_eval_dataset
"""
predictions = trainer.predict(small_eval_dataset)
print(list(np.argmax(predictions.predictions, axis=-1)))

"""
Now We will call Inferance by Loading the save tokeniizer and fine tuned model

"""
tokenizer = AutoTokenizer.from_pretrained('./save_tokenizer/')
model = AutoModelForSequenceClassification.from_pretrained("./test_trainer/", num_labels=2)
#calling prediction

print("\n\nLabel 0 = Functional Deficits\nLabel 1 = Delay Reason\nLabel 2 = Cause\n\n")
for i in range(20):
    print("Enter Text")
    text=str(input())
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)                                                                                         
    result=classifier(text)
    print("\n\n",result)
