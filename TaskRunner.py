__author__ = 'luowen'
import argparse
from Tasks import UserTask
import time
"create entrance of project "

def main():
    parserObj = argparse.ArgumentParser()

    parserObj.add_argument("task", help="Please input a task name", choices=["UserTask", "StatisticsTask"])
    parserObj.add_argument("--business", help="please input task business name", default="start")
    options = parserObj.parse_args()

    if options.task == "UserTask":
        userTask = UserTask.UserTask()
        timeStamp = time.time()
        userTask.start(timeStamp)

if __name__ == "__main__":
    main()
