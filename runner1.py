import subprocess

if __name__ == "__main__":
    subprocess.run(["make", "build"])

    print("verify memory errors")
    subprocess.run(["valgrind", "--tool=memcheck", "./program"])
    
    print("check threads error (concurrency issue detection)")
    subprocess.run(["valgrind", "--tool=helgrind", "./program"])
    
    print("check threads error (advanced mapping)")
    subprocess.run(["valgrind", "--tool=drd", "./program"])

    print("mapping memory consuming")
    subprocess.run(["valgrind", "--tool=massif", "./program"])

