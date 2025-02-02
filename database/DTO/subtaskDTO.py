class SubtaskDTO:
    def __init__(self, id, subtask, task, status):
        self.id = id
        self.subtask = subtask
        self.task = task
        self.status = status

    def __repr__(self):
        return f'TaskDTO(id={self.id}, name={self.subtask}, name={self.task}, status={self.status})'