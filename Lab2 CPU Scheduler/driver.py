#driver.py
from cpu_scheduler import CPU_Scheduler

def main():
    file_name = input("Enter the name of the input file: ")
    CPUSched = CPU_Scheduler(file_name)
    CPUSched.run()

main()