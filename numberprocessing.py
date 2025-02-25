import logging
import random

def setup_logger():
    logging.basicConfig(
        filename="app.log", 
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def process_numbers(numbers):
    for num in numbers:
        try:
            if num < 0:
                raise ValueError(f"Negative number encountered: {num}")
            logging.info(f"Processing number: {num}")
        except ValueError as e:
            logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    setup_logger()
    logging.info("Script started")
    numbers = [random.randint(-5, 10) for _ in range(10)]
    process_numbers(numbers)
    logging.info("Script finished")
