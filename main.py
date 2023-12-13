import logging
import random
from functools import wraps

logging.basicConfig(
    filename='triangle.log',
    format="{filename} - {asctime} - {msg}",
    style="{",
    level=logging.INFO)
logger = logging.getLogger("app")


def log_func(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f"Function {func.__name__} has been successfully decorated")
                return result
            except Exception as e:
                logger.error(f"Exception {e}")
                raise

        return wrapper

    return decorator


@log_func(logger)
def triangle(sideList):
    try:
        if sideList[0] > 0 and sideList[1] > 0 and sideList[2] > 0:
            for i in range(len(sideList)):
                sideSum = 0
                for j in range(len(sideList)):
                    if i != j:
                        sideSum += sideList[j]
                if sideList[i] >= sideSum: return print("Треугольник не существует")
            if len(set(sideList)) == 1:
                return print("Треугольник существует" + "\n" + "Треугольник равносторонний")
            elif len(set(sideList)) == 2:
                return print("Треугольник существует" + "\n" + "Треугольник равнобедренный")
            elif len(set(sideList)) == 3:
                return print("Треугольник существует" + "\n" + "Треугольник разносторонний")
        else: raise ValueError("Neagtive length value has been taken")
    except ValueError as e:
        logger.error(e)


if __name__ == '__main__':
    for i in range(10):
        triangle([random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)])
