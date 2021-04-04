import numpy as np

# Function to get the idle time Xi on machine B for all jobs
def get_idle_time(data, optimal_seq):
    # Store the Ai's & Bi's from the given data
    a = [data[0][i-1] for i in optimal_seq]
    b = [data[1][i-1] for i in optimal_seq]

    # This array will store the idle times on machine B (Xi) for each job i 
    x = []

    for i in range(data.shape[1]):
        x.append(max(sum(a[:i+1]) - sum(b[:i]) - sum(x[:i]), 0.0))
    
    return x

# Function to obtain the optimal sequence for a n/2 scheduling problem using Johnson's algorithm
def johnsons_algo(x):
    # Create a placeholder to store the optimal sequence of jobs
    optimal_seq = np.zeros(x.shape[1], dtype=int)

    front = 0
    back = x.shape[1] - 1

    # Obtain the indices of the elememnts of the matrix after sorting in ascending order. 
    # These indices will be used in scheduling
    sorted_indices = np.argsort(x.flatten())

    # Repeat the scheduling process until all the jobs are scheduled
    i = 0
    while front <= back:
        smallest_elem_index = np.unravel_index(sorted_indices[i], x.shape)

        # Select the job with the smallest Ai or Bi
        candidate_job = smallest_elem_index[1] + 1

        # Since the way we select the next smallest Ai or Bi does not guarantee that 
        # a 'unique' (unscheduled) job is selected, we perform an extra check to include 
        # this job only if it doesn't already exist in the array containing our optimal sequence
        if candidate_job not in optimal_seq:
            # If the smallest value belongs to machine A, add the Job to start of scheduling
            if smallest_elem_index[0] == 0:
                optimal_seq[front] = candidate_job
                front += 1
            # If the smallest value belongs to machine B, add the Job to end of scheduling
            elif smallest_elem_index[0] == 1:
                optimal_seq[back] = candidate_job
                back -= 1
        
        i += 1

    return optimal_seq


def shop_floor_scheduling(schedule_file):
    x = np.genfromtxt(schedule_file, delimiter=',')
    opt_seq = johnsons_algo(x)
    idle_time = get_idle_time(x, opt_seq)


    print("Optimal Sequence of Jobs:\t", *opt_seq)
    print("Idle Time Xi on Machine B for jobs:")
    for i, time in enumerate(idle_time):
        print(f"\tX{i+1} = {time}")
    print("Total idle time on Machine B:\t", sum(idle_time))
    print("Total processing time:\t\t", sum(idle_time) + sum(x[1][:]))



def main():
    shop_floor_scheduling("schedule.csv")

if __name__ == "__main__":
    main()