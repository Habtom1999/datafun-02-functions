"""
Custom Math module created by Habtom Woldu.
Date: 5/20/2023. The purpouse of this module is to import math 
and do some basic mathemaical operations. 
and if things don't work provide a custom message.

Use try / except / finally whenever a valid function could cause an error
e.g.,
- a number is not valid such as a negative radius or age
- a string is empty or missing
- the requested resouce could not be found
"""

import math

from util_datafun_logger import setup_logger

logger, logname = setup_logger(__file__)



def get_rectangle_area_given_(height,width):
    """
    Return area of a rectangle given the heightand width.

    @param height,width: the area of rectangle
    @return: the area of the rectangle
    @raise Exception: if hegiht,width is not a number

    """

    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"get_rectangle_area_given_({height},{width})")

    try: 
        area = height * width
        logger.info(f"The rectangle area is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None


def get_area_of_rectangle(height_list, width_list):
    """
    Return a list with the area of each rectangle.
    
    @param height_list: a list of height values
    @param width_list: a list of width values
    @return: a list of areas of each rectangle
    """
    logger.info(f"get_area_of_rectangle({height_list}, {width_list})")

    if len (height_list) == 0 and len(width_list) == 0:
        logger.error("Please add some items to the list. Nothing to do.")
        quit() # quit the program

    area_list = [] # empty list to hold the areas

    # for every element in the list passed in 
    for h,w in zip(height_list,width_list):

        try:
            area = get_rectangle_area_given_(h,w)
            logger.info(f"r = {h,w}, area={area}")
            area_list.append(area)

        except Exception as ex:
            logger.error(f"height,width = {h,w}, Error: {ex}")


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# Literally: "if this module name == the name of the main running module"
# (as opposed to being imported by another module like we do the logger),
# then, follow these instructions.
if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")

    logger.info("TRY:get_area_of_rectangle(height_list, width_list)() function with a different values.")
    get_area_of_rectangle([5,3,4], [2,3,6])
    get_area_of_rectangle(-16,4)
    get_area_of_rectangle(math.inf)
    logger.info("")

    logger.info(" Try: get_area_of_rectangle(height, width)() function with a list that may include BAD values")
    bad_list = [([-5,0,],[0,-2], math.inf, '30')]
    get_area_of_rectangle(bad_list)

    print("Done. Please check the log file for more details.")


