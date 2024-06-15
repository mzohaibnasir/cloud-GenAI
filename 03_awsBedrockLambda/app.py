# to get lateset boto3 version

# pip install boto3 -t python/
# zip that folder and add it as boto3 layer

import boto3
import botocore.config
import json
from datetime import datetime

# boto3 to invoke FMs


s3_bucket = "awsbedrockbucketc1"


# blog generation
def blog_generation_using_bedrock(blogTopic: str) -> str:
    prompt = f"""Write a 200 words blog on the topic { blogTopic}
    """

    # prompt = f"""<s>[INST]Human: Write a 200 words blog on the topic { blogTopic}
    #  Assistant:[/INST]""" # for llama

    body = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "stopSequences": [],
            "temperature": 0.5,
            "topP": 1,
        },
    }
    accept = "application/json"
    content_type = "application/json"

    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="ap-southeast-2",
            config=botocore.config.Config(
                read_timeout=300, retries={"max_attempts": 3}
            ),
        )
        response = bedrock.invoke_model(
            body=json.dumps(body),
            modelId="amazon.titan-text-lite-v1",
            accept=accept,
            contentType=content_type,
        )
        response_content = response.get("body").read()
        response_data = json.loads(response_content)
        print(response_data)
        blog_details = response_data["results"][0]["outputText"]
        print(blog_details)

        return blog_details

    except Exception as e:
        print(f"Error generating the blog: {e}")
        # return "xxxxxxxxxx"


def save_blog_details_in_s3(s3_key, s3_bucket, generate_blog):
    s3 = boto3.client("s3")

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)
        print("text saved to s3")
    except Exception as e:
        print("Error saving!: save_blog_details_in_s3()")


def lambda_handler(event, context):
    print(f"event: {event}")
    body = json.loads(event["body"])
    print(f"body: {body}")
    blogtopic = body["blog_topic"]
    print(f"blogtopic: {blogtopic}")

    generate_blog = blog_generation_using_bedrock(
        blogTopic=blogtopic,
    )
    if generate_blog:
        current_time = datetime.now().strftime("%H%M%S")
        s3_key = f"blog_ouput/{current_time}.txt"
        # s3_bucket = "awsbedrockbucketc1"
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
