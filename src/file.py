import os


class Write:
    """_class that handels writing to the result_
    """
    def __init__(self):
        self.name = os.path.dirname(__file__)

    # append with the result

    def print(self,time,info):
        """_method that actually wirtes the result_

        Args:
            time (_str_): _amount of time that has passed until result is written down_
            info (_str_): _board info on what to write down_
        """
        if info is None:
            pass
        with open(os.path.join(self.name,"results", "result.txt"), "a", encoding="utf-8") as f:
            f.write(f"{info}{time} seconds \n")
