"""
Logging exercise
Author: Schubert Carvalho
Date: Nov 2022
"""
import logging

logging.basicConfig(
    filename="./results.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


def sum_vals(num_one, num_two):
    """
    Args:
        num_one: (int)
        num_two: (int)
    Return:
        num_one + num_two (int)
    """
    try:

        logging.info("%s, %s", num_one, num_two)
        assert isinstance(num_one, int)
        assert isinstance(num_two, int)
        logging.info("SUCCESS: it looks like the values are int")

        return num_one + num_two

    except AssertionError:

        logging.error("it appears input_a or input_b are not ints")

        return None


if __name__ == "__main__":
    sum_vals("no", "way")
    sum_vals(4, 5)
