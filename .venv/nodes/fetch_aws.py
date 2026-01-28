import boto3
def fetch_aws(state: dict) -> dict:
    """
    Fetch live AWS pricing. 
    LangGraph passes the 'state' dict here, not individual arguments.
    """
    client = boto3.client("pricing", region_name="us-east-1")

    response = client.get_finalProducts(
        ServiceCode = "AmazonEC2",
        MaxResults = 1
    )

    state["aws_data"] = {
        "raw_pricing": response["PriceListings"][0][:500]
    }

    return state