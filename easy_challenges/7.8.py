import time

class StopWatch:
    def __init__(self, startTime = time.time()):
        self.__startTime = startTime
        self.__endTime = 0

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime
    
        

    def stop(self):
        self.__endTime = time.time()

    

    def start(self):
        self.__startTime = time.time()

    def getElapsedTime(self):
        return self.__endTime - self.__startTime

def main():
    count = 0
    Timer = StopWatch()
    for i in range(1, 1000001):
        count += i
        
    Timer.stop()
    total_Time = Timer.getElapsedTime()
    print("Total time elapsed to count to 1,000,000: ",total_Time," seconds")

if __name__ == '__main__':
    main()
