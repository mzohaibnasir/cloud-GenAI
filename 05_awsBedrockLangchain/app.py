import json
import os
import sys
import boto3
import botocore

# we will be using titan embedding model

from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.llms import Bedrock

# Data ingestion
import numpy as np
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader


# vector embeddings
from langchain_community.vectorstores import FAISS

# LLM
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain


# bedrock client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="ap-southeast-2"),
)
bedrock_embeddings = BedrockEmbeddings(modelId="amazon.titan-embed-text-v1",client= bedrock)



# data ingestion
def data_ingestion():
    loader = PyPDFDirectoryLoader('data')
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    return docs

# vector embeddings

def get_vector_store(docs):
    vectorstore_faiss = FAISS.from_documents(
        docs, bedrock_embeddings)
    vectorstore_faiss.save_local("faiss_index")
    
def get_claude_llm():
    llm=Bedrock(model_id="amazon.titan-text-lite-v1",client=bedrock,
                model_kwargs={ 
                "maxTokenCount": 512,
                "stopSequences": [],
                "temperature": 0.5,
                "topP": 1,

                    })
    
    return llm



# write code to invoke bedrock models
def invoke_bedrock_models():
    docs = data_ingestion()
    get_vector_store(docs)
    llm = get_claude_llm(