import logging

#logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmeticApp")

def Add(a,b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def Subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def Multiply(a,b):
    result = a * b
    logger.debug(f"multiplying {a} * {b} = {result}")
    return result

def Divide(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
Add(10,15)
Subtract(15,10)
Multiply(5,3)
Divide(10,10000)







