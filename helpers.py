# no modificar
def retrieve_phone_code(driver) -> str:
    import json
    import time
    from selenium.common import WebDriverException

    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance')
                    if log.get("message") and 'api/v1/number?number' in log["message"]]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
                if code:
                    return code
        except WebDriverException:
            time.sleep(1)
    raise Exception("No se encontró el código de confirmación del teléfono.")