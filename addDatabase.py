import os
import django
import random
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWork.settings')

django.setup()

from application.models import Job, User,Application,Feedback  # 替换myapp为你的应用名

# employer = User.objects.get(id=4)  # ID为4(雇主)
# for _ in range(5):  # 生成5个示例
#     job = Job(
#         employer=employer,
#         type=random.choice(Job.JOB_TYPE_CHOICES)[0],
#         requirement=random.choice(Job.JOB_REQUEST_CHOICES)[0],
#         remote=random.choice(Job.JOB_REMOTE_CHOICES)[0],
#         industry=random.choice(Job.JOB_INDUSTRY_CHOICES)[0],
#         title=f"Job Title {_}",
#         description="A job description here",
#         postcode="G1 XXX",
#         start_date=timezone.now(),
#         end_date=timezone.now() + timedelta(days=random.randint(1, 30)),
#         city="Glasgow",
#         salary=random.uniform(20000, 50000),
#         other="Some other details here"
#     )
#     job.save()
# print("Jobs created successfully.")


# user = User.objects.get(id=3)  # 获取ID为3的用户
# jobs = [Job.objects.get(id=1), Job.objects.get(id=2)]  # 获取ID为1和2的职位
#
# # 随机生成Application实例
# for job in jobs:
#     for _ in range(2):  # 每个职位生成2个示例
#         application = Application(
#             user=user,
#             job=job,
#             apply_date=timezone.now(),
#             status=random.choice(Application.STATUS_TYPE_CHOICES)[0]
#         )
#         application.save()
#
# print("Applications created successfully.")

# user = User.objects.get(id=3)
# job = Job.objects.get(id=1)

# # 创建Feedback实例
# for _ in range(3):  # 创建3个示例
#     feedback = Feedback(
#         user=user,
#         job=job,
#         rate=random.randint(1, 5),  # 随机生成1到5之间的整数
#         comment='Yeah!',  # 示例评论文本
#         date=timezone.now()  # 当前时间
#     )
#     feedback.save()
#
# print("Feedback entries created successfully.")

