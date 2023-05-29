from fastapi import FastAPI

import utils
import time
import logging

app = FastAPI()
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.DEBUG)


@app.get("/ping")
def ping():
    return {"response": "pong"}


@app.get("/matrix/{size}")
def matrix_multiplication(size: int):
    matrix_a = utils.create_non_singular_matrix(size=size)
    start = time.time()
    logger.info("Creating matrix took %.5f", start - time.time())
    matrix_b = matrix_a
    start = time.time()
    matrix_c = utils.multiply_matrix(matrix_a=matrix_a, matrix_b=matrix_b)
    logger.info("Multiplying matrix took %.5f", start - time.time())
    determinant = utils.calculate_determinant(matrix=matrix_c)
    start = time.time()
    logger.info("Calculating determinant of matrix took %.5f", start - time.time())
    logger.info("Determinant is %.5f", determinant)

    return {"code": 200, "determinant": str(round(determinant, 5))}





