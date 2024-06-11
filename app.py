# to get lateset boto3 version

# pip install boto3 -t python/
# zip that folder and add it as boto3 layer

import boto3
import botcore.config
import json
from datetime import datetime

# boto3 to invoke FMs


# blog generation
def blog_generation_using_bedrock(blogTopic: str) -> str:
    prompt = f"""Write a 200 words blog on the topic { blogTopic}
    """

    # prompt = f"""<s>[INST]Human: Write a 200 words blog on the topic { blogTopic}
    #  Assistant:[/INST]""" # for llama

    body = {"prompt": prompt, "maxTokenCount": 512, "temperature": 0.5, "topP": 1}

    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="ap-southeast-2",
            config=botocore.config.Config(
                read_timeout=300, retries={"max_attempts": 3}
            ),
        )
        response = bedrock.invoke_model(
            body=json.dumps(body), model_id="amazon.titan-text-lite-v1"
        )
        response_content = response.get("body").read()
        response_data = json.loads(response_content)
        print(response_data)
        blog_details = response_data["generation"]
        return blog_details

    except Exception as e:
        print(f"Error generating the blog: {e}")
        return " "


def save_blog_details_in_s3(s3_key, s3_bucket, generate_blog):
    s3 = boto3.client("s3")

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)
        print("text saved to s3")
    except Exception as e:
        print("Error saving")


def lamda_handler(event, context):
    event = json.loads(event["body"])
    blogtopic = event["blog_topic"]
    generate_blog = blog_generation_using_bedrock(
        blogTopic=blogtopic,
    )
    if generate_blog:
        curren_time = datetime.now().strftime("%H%M%S")
        s3_key = f"blog_ouput/{current_time}.txt"
        s3_bucket = "aws_bedrock"
        save_blog_details_in_s3(
            s3_key=s3_key, s3_bucket=s3_bucket, generate_blog=generate_blog
        )
    else:
        print("No blog was generated.")

    return {"statusCode": 200, "body": json.dumps("Blog generation done")}


##################################3
{
    "modelId": "amazon.titan-text-lite-v1",
    "contentType": "application/json",
    "accept": "application/json",
    "body": '{"inputText":"this is where you place your input text","textGenerationConfig":{"maxTokenCount":4096,"stopSequences":[],"temperature":0,"topP":1}}',
}
