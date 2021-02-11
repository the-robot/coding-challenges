// https://www.geeksforgeeks.org/maximum-cpu-load-from-the-given-list-of-jobs/

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Job {
    public:
        int start = 0;
        int end = 0;
        int cpuLoad = 0;
    
        Job(int start, int end, int cpuLoad) {
            this->start = start;
            this->end = end;
            this->cpuLoad = cpuLoad;
        }
};

class MaximumCPULoad {
    public:
        static int findMaxCPULoad(vector<Job> &jobs) {
            // sort the jobs
            sort(
                jobs.begin(),
                jobs.end(),
                [](const Job &x, const Job &y) -> bool {
                    return x.start < y.start;
                }
            );

            int maxCPULoad = 0;
            int currentCPULoad = 0;
            priority_queue<Job, vector<Job>, endCompare> minHeap; // FIFO

            for (auto job : jobs) {
                // remove all jobs that have ended
                while (!minHeap.empty() && job.start > minHeap.top().end) {
                    currentCPULoad -= minHeap.top().cpuLoad;
                    minHeap.pop();
                }

                // add the current job into cpu load
                minHeap.push(job);
                currentCPULoad += job.cpuLoad;
                maxCPULoad = max(maxCPULoad, currentCPULoad);
            }

            return maxCPULoad;
        }
    
    private:
        struct endCompare {
            bool operator()(const Job &x, const Job &y) {
                return x.end > y.end;
            }
        };
};

int main() {
    vector<Job> input {
        {1, 4, 3},
        {2, 5, 4},
        {7, 9, 6},
    };
    int maxCPULoad = MaximumCPULoad::findMaxCPULoad(input);
    if (maxCPULoad != 7) {
        cout << "Wrong answer." << endl;
    }

    input = {
        {6, 7, 10},
        {2, 4, 11},
        {8, 12, 15},
    };
    maxCPULoad = MaximumCPULoad::findMaxCPULoad(input);
    if (maxCPULoad != 15) {
        cout << "Wrong answer." << endl;
    }

    input = {
        {1, 4, 2},
        {2, 4, 1},
        {3, 6, 5},
    };
    maxCPULoad = MaximumCPULoad::findMaxCPULoad(input);
    if (maxCPULoad != 8) {
        cout << "Wrong answer." << endl;
    }

    return 0;
}
