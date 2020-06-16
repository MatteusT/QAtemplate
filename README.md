# Question-Answering Application Template

This repo is a template for setting up a simple Question-Answering application using Django. 

## Set-up

To get the application set up you will only need to be concerned with two files: 
 
- `qa_gui/apps.py`: This is where the classes and the models are initated.  
- `qa_gui/code.py`: Here is where the actual algoritms are executed.

## Instructions

This application considers 3 methods:
 - Extract the paragraphs from the documents/unstructured data. Here, this will consist of two functions that should be in `qa_gui/apps.py`.
 - Find the paragraphs best suited to the question given. This will require a model to ge a representation of the paragraphs and the question. 
 The initialization of the the vectorizer should be in `qa_gui/apps.py` and could also use the paragraphs. The function which will actually match the question to the paragraphs should be in `qa_gui/code.py`.
 - Extract the answer given the paragraph and question. Here again the initialization of the QA model should be in `qa_gui/apps.py` and the function used to extract the answer should be in `qa_gui/code.py`.
 
 