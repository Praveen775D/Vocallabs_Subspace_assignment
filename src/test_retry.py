from utils.retry import retry


counter = 0


def test_function():

    global counter

    counter += 1

    if counter < 3:

        raise Exception("Failed")

    return "Success"


print(
    retry(test_function)
)