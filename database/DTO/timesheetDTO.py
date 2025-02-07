from  database.models.timesheet import Timesheet

class TimesheetDTO:
    def __init__(self, timesheet):
        self.id = timesheet.id
        self.operator = timesheet.operator
        self.projectId = timesheet.projectId
        self.projectCode = "projectCode"
        self.projectName = "projectName"        
        self.unit_name = timesheet.unit_name        
        self.subtaskId = timesheet.sub_taskId
        self.subtaskName = "subtaskName"
        self.taskName = "taskName"
        self.type_feature = timesheet.type_feature
        self.type_task = timesheet.type_task
        self.comments = timesheet.comments
        self.start_time = timesheet.start_time
        self.end_time = timesheet.end_time
        self.total_time = "totalTime"
        self.status = timesheet.status

    def __repr__(self):
        return (f'TimesheetDTO(id={self.id}, operator={self.operator}, projectId={self.projectId}, '
                f'projectCode={self.projectCode}, projectName={self.projectName}, unit_name={self.unit_name}, '
                f'subtaskId={self.subtaskId}, subtaskName={self.subtaskName}, taskName={self.taskName}, '
                f'type_feature={self.type_feature}, type_task={self.type_task}, comments={self.comments}, '
                f'start_time={self.start_time}, end_time={self.end_time}, total_time={self.total_time}, '
                f'status={self.status})')