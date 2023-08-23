import requests

urls = {"fun_data": "http://numbersapi.com/{month}/{day}/date"}


# if are more then one api calls is better to use async aproch
# as for this exemple is not worth
def get_fun_fact(month, day):
    try:
        url = urls.get("fun_data").format(month=month, day=day)
        r = requests.get(url)
    except Exception as e:
        raise f"there is an exceprion on ApiRequest:{e}"
    return r.text
