import subprocess
import time
import psutil
import humanfriendly

class Tracer:
    _startTime = 0
    _residentSetSize = 0
    _virtualMemorySize = 0
    _uniqueSetSize = 0

    def run(self, programName):
        self.start()

        program = subprocess.Popen(f"./{programName}")
        SLICE_IN_SECONDS = 1
        self._residentSetSize = 0
        self._virtualMemorySize = 0
        self._uniqueSetSize = 0
        while program.poll() is None:
            process = psutil.Process(program.pid)
            self._residentSetSize = max(self._residentSetSize, process.memory_full_info().rss)
            self._virtualMemorySize = max(self._virtualMemorySize, process.memory_full_info().vms)
            self._uniqueSetSize = max(self._uniqueSetSize, process.memory_full_info().uss)
            time.sleep(SLICE_IN_SECONDS)
            
        self.stop()

    def start(self):
        self._startTime = time.time()  # Return the time in seconds since the epoch as a floating point number
        self._residentSetSize = 0
        self._virtualMemorySize = 0
        self._uniqueSetSize = 0

    def stop(self):
        endTime = time.time() # Return the time in seconds since the epoch as a floating point number

        elapsedTimeInSeconds = endTime - self._startTime
        print(f"Elapsed Time = {elapsedTimeInSeconds} seconds")
        print(f"Resident Set Size (RSS) = {humanfriendly.format_size(self._residentSetSize)}")
        print(f"Virtual Memory Size (VMS) = {humanfriendly.format_size(self._virtualMemorySize)}")
        print(f"Unique Set Size (USS) = {humanfriendly.format_size(self._uniqueSetSize)}")

if __name__ == "__main__":
    subprocess.run(["make", "build"])

    tracer = Tracer()
    tracer.run("program")