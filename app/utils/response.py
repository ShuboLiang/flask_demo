from flask import make_response, jsonify


def json_response(data=None, message="success", status=200, success=True, **kwargs):
    """
    生成一个通用的 JSON 格式响应。

    通过传入状态码、成功标志、消息和数据，创建一个 Flask Response 对象。
    这个函数也接受任意额外的关键字参数，这些参数将被包含在响应的 JSON 对象中。

    Args:
        status (int, optional): HTTP 状态码。例如，200 表示成功，404 表示未找到等。默认为 200。
        success (bool, optional): 表示响应是否成功的布尔值。默认为 True。
        message (str, optional): 成功或错误的相关信息。默认为 None。
        data (dict, list, optional): 要返回的数据，可以是字典或列表。默认为 None。
        **kwargs: 允许添加任何额外的关键字参数到 JSON 响应对象。

    Returns:
        Response: Flask Response 对象，包含了 JSON 格式的响应体和状态码。
    """
    response = {"success": success, "message": message, "data": data}
    # 将 kwargs 中的额外参数添加到响应中
    response.update(kwargs)
    return make_response(jsonify(response), status)


def json_error_response(message="error", status=500, success=False, **kwargs):
    """
    生成一个通用的 JSON 格式错误响应。

    通过传入状态码、成功标志、消息和数据，创建一个 Flask Response 对象。
    这个函数也接受任意额外的关键字参数，这些参数将被包含在响应的 JSON 对象中。

    Args:
        status (int, optional): HTTP 状态码。例如，200 表示成功，404 表示未找到等。默认为 500。
        success (bool, optional): 表示响应是否成功的布尔值。默认为 False。
        message (str, optional): 成功或错误的相关信息。默认为 "error"。
        **kwargs: 允许添加任何额外的关键字参数到 JSON 响应对象。

    Returns:
        Response: Flask Response 对象，包含了 JSON 格式的响应体和状态码。
    """
    response = {"success": success, "message": message}
    # 将 kwargs 中的额外参数添加到响应中
    response.update(kwargs)
    return make_response(jsonify(response), status)
