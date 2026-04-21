import os


class Write:
    def __init__(self):
        self.name = os.path.dirname(__file__)

    # append with the result

    def print(self,time,info):
        if info == None:
            pass
        with open(os.path.join(self.name,"results", "result.txt"), "a", encoding="utf-8") as f:
            f.write(f"{info}{time} seconds \n")
