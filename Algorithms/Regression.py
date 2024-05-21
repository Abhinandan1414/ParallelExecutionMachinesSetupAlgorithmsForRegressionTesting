import math
import pandas
import os


def weighted_split_test_exec_time_list(original_test_exec_time_list, weight_list, absolute_machine_speeds):
    machine_i_test_set = []
    machine_i_test_set_exec_time = []
    prev_index = 0
    
    for weight in weight_list:
        next_index = prev_index + math.ceil((len(original_test_exec_time_list) * weight))
        machine_i_test_set.append(original_test_exec_time_list[prev_index: next_index])
        prev_index = next_index
        
    for i in range(len(weight_list)):
        machine_i_test_set_exec_time.append(
            sum(machine_i_test_set[i])/absolute_machine_speeds[i])
    
    print(machine_i_test_set)
    for i in range(len(weight_list)):
        print("Machine",i,"Will execute the following test cases",machine_i_test_set[i],"in",machine_i_test_set_exec_time[i],"unit time")
       
        
    local_sorted_execution_time_on_machines = sorted(machine_i_test_set_exec_time,reverse=True)
    print("Longest time is", local_sorted_execution_time_on_machines[0],"Which is effective execution time")
    
    print("All Machines will put together will be busy for",sum(machine_i_test_set_exec_time))
       


def identical_machines_total_execution_time(x, n):
    machine_i_test_set = []
    machine_i_test_set_exec_time = []
    x = sorted(x, reverse=True)
    
    for i in range(n):
        machine_i_test_set.append([])
        
    for i in range(len(x)):
        machine_i_test_set[i % n].append(x[i])

    for i in range(n):
        machine_i_test_set_exec_time.append(sum(machine_i_test_set[i]))
    
    #print(machine_i_test_set)
    
    for i in range(n):
        print("Machine",i,"Will execute the following test cases",machine_i_test_set[i],"in",machine_i_test_set_exec_time[i],"unit time")
        #print("Test Suite on Machine", i, "Will run for", machine_i_test_set_exec_time[i],"Units of Time")

        
    local_sorted_execution_time_on_machines = sorted(machine_i_test_set_exec_time,reverse=True)
    print("Longest time is", local_sorted_execution_time_on_machines[0],"Which is effective execution time")
    
    print("All Machines will put together will be busy for",sum(machine_i_test_set_exec_time))


def main():
    df = pandas.read_csv(os.path.join(os.getcwd(), "Regression\\testexecutiondata.csv"),
                         sep=',')

    data_set = df["execution_time"].to_list()
    
    print("Data set is",data_set)

    absolute_machine_speeds = [1, 2, 2, 1]
    weighted_machine_speeds = [.16, .32, .32, .16]
    identical_machine_speeds = [1, 1, 1, 1]
    
    identical_machines_total_execution_time(
        data_set, len(identical_machine_speeds))

    weighted_split_test_exec_time_list(data_set, weighted_machine_speeds, absolute_machine_speeds)
    
    
main()
