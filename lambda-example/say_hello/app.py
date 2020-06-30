import json


def lambda_handler(event, context):
    try:
        input_body = json.loads(event["body"])
        name = input_body["name"]
        greeting = f"Hello {name}!"
        body = json.dumps({"message": greeting})

        if (
            name.lower() == "teapot"
        ):  # if the name is Teapot, return a teapot greeting and the teapot code
            return {"statusCode": 418, "body": body}
        else:  # otherwise, returning the greeting for that name and a 200 code
            return {"statusCode": 200, "body": body}

    except KeyError:
        return {"statusCode": 400}

    except IndexError:
        return {"statusCode": 400}
