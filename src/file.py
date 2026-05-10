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
            info (_(int,int,int,int)_): _board info on what to write down; width, height, mincount, state (win,lose,reset)_
        """
        if info is None:
            pass

        if info[3] == 3:
            with open(os.path.join(self.name,"results", "result.txt"), "a", encoding="utf-8") as f:
                f.write(f"reset with a {info[0]} x {info[1]} grid that had {info[2]} mines, in a time of {time} \n")
        if info[3] == 2:
            with open(os.path.join(self.name,"results", "result.txt"), "a", encoding="utf-8") as f:
                f.write(f"lost with a {info[0]} x {info[1]} grid that had {info[2]} mines, in a time of {time}\n")
        if info[3] == 1:
            with open(os.path.join(self.name,"results", "result.txt"), "a", encoding="utf-8") as f:
                f.write(f"won with a {info[0]} x {info[1]} grid that had {info[2]} mines, in a time of {time}\n")
