def taskAssignment(k, tasks):
    # Write your code here.
    pairedTask = []
    taskDurationsToIndices = getTaskDurationsToIndices(tasks)

    sortedTasks = sorted(tasks)
    for idx in range(k):
        task1Duration = sortedTasks[idx]
        task2Duration = sortedTasks[len(tasks) - 1 - idx]
        task1Index = taskDurationsToIndices[task1Duration].pop()
        task2Index = taskDurationsToIndices[task2Duration].pop()
        pairedTask.append([task1Index, task2Index])

    return pairedTask


def getTaskDurationsToIndices(tasks):
    taskDurationsToIndices = {}

    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration].append(idx)
        else:
            taskDurationsToIndices[taskDuration] = [idx]

    return taskDurationsToIndices
