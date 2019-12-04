
def get_int_value(value, default_value):
    try:
        value = int(value)
    except:
        value = default_value
    return value