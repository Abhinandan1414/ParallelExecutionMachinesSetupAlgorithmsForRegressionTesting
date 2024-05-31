import math
import pandas
import os

def identical_split_test_exec_time_list_assymetrical_speed_round_robin_post_sort(original_test_exec_time_list, absolute_machine_speeds):
    print('identical_split_test_exec_time_list_assymetrical_speed_round_robin_post_sort at work')
    machine_i_test_set = []
    machine_i_test_set_exec_time = []
    original_test_exec_time_list = sorted(original_test_exec_time_list, reverse=True)
    absolute_machine_speeds = sorted(absolute_machine_speeds, reverse=True)
    
   
    n = len(absolute_machine_speeds)
    
    for i in range(n):
        machine_i_test_set.append([])
    
    for i in range(len(original_test_exec_time_list)):
        machine_i_test_set[i % n].append(original_test_exec_time_list[i])
    
           
    for i in range(len(absolute_machine_speeds)):
        machine_i_test_set_exec_time.append(
            sum(machine_i_test_set[i])/absolute_machine_speeds[i])
    
    print(machine_i_test_set)
    for i in range(len(absolute_machine_speeds)):
        print("Machine",i,"Will execute the following test cases",machine_i_test_set[i],"in",machine_i_test_set_exec_time[i],"unit time")
    
    local_sorted_execution_time_on_machines = sorted(machine_i_test_set_exec_time,reverse=True)
    print("Longest time is", local_sorted_execution_time_on_machines[0],"Which is effective execution time")
    
    print("All Machines will put together will be busy for",sum(machine_i_test_set_exec_time))


def identical_split_test_exec_time_list_assymetrical_speed(original_test_exec_time_list, absolute_machine_speeds):
    print('identical_split_test_exec_time_list_assymetrical_speed at work')
    machine_i_test_set = []
    machine_i_test_set_exec_time = []
    prev_index = 0
    original_test_exec_time_list = sorted(original_test_exec_time_list, reverse=True)
    absolute_machine_speeds = sorted(absolute_machine_speeds, reverse=True)
    
    for i in range(len(absolute_machine_speeds)):
        next_index = prev_index + len(original_test_exec_time_list) // len(absolute_machine_speeds)
        machine_i_test_set.append(original_test_exec_time_list[prev_index: next_index])
        prev_index = next_index
        
    for i in range(len(absolute_machine_speeds)):
        machine_i_test_set_exec_time.append(
            sum(machine_i_test_set[i])/absolute_machine_speeds[i])
    
    print(machine_i_test_set)
    for i in range(len(absolute_machine_speeds)):
        print("Machine",i,"Will execute the following test cases",machine_i_test_set[i],"in",machine_i_test_set_exec_time[i],"unit time")
       
        
    local_sorted_execution_time_on_machines = sorted(machine_i_test_set_exec_time,reverse=True)
    print("Longest time is", local_sorted_execution_time_on_machines[0],"Which is effective execution time")
    
    print("All Machines will put together will be busy for",sum(machine_i_test_set_exec_time))

def weighted_split_test_exec_time_list_assymetrical_speed(original_test_exec_time_list, weight_list, absolute_machine_speeds):
    print('weighted_split_test_exec_time_list_assymetrical_speed at work')
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
       


def identical_split_test_exec_time_list_symetrical_speed(x, n):
    print('identical_machines_total_execution_time at work')
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
    df = pandas.read_csv(os.path.join(os.getcwd(), "Algorithms\\testexecutiondata.csv"),
                         sep=',')

    data_set = df["execution_time"].to_list()
    
    print("Data set is",data_set)

    absolute_machine_speeds = [1, 2, 2, 1]
    weighted_machine_speeds = [.16, .32, .32, .16]
    identical_machine_speeds = [1, 1, 1, 1]
    
    identical_split_test_exec_time_list_symetrical_speed(data_set, len(identical_machine_speeds))

    weighted_split_test_exec_time_list_assymetrical_speed(data_set, weighted_machine_speeds, absolute_machine_speeds)
    identical_split_test_exec_time_list_assymetrical_speed(data_set, absolute_machine_speeds)
    identical_split_test_exec_time_list_assymetrical_speed_round_robin_post_sort(data_set, absolute_machine_speeds)
    
main()
