import datetime
user_data_base = {}

class user:

    def __init__(self, name, bussiness_info):
        self.name = name
        self.business_info = bussiness_info

    def __str__(self):
        return self.name



class business_info:
    def __init__(self, name, description, work_days, start_working_day, end_working_day, tfou, hmucbaot, schedule):
        self.name = name
        self.description = description
        self.work_days = work_days
        self.start_working_day = start_working_day
        self.end_working_day = end_working_day
        self.tfou = tfou
        self.schedule = schedule
        self.hmucbaot = hmucbaot

    def time_management(self):
        # преобразование строк в объекты datetime
        self.start_working_day = datetime.datetime.strptime(self.start_working_day, '%H:%M')
        self.end_working_day = datetime.datetime.strptime(self.end_working_day, '%H:%M')
        self.tfou = datetime.timedelta(minutes=self.tfou)

        # вычисление количества интервалов
        total_time = self.end_working_day - self.start_working_day
        intervals = int(total_time / self.tfou)

        # создание списка для записи по времени
        schedule = []
        current_time = self.start_working_day
        for i in range(intervals):
            schedule.append(current_time.strftime('%H:%M'))
            current_time += self.tfou
        self.schedule = schedule

