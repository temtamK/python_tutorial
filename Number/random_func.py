from random import *

print(random()) # 0.0 ~ 1.0�̸��� ������ �� ����
print(random() * 10) # 0.0 ~ 10.0 �̸��� ������ �� ����
print(int(random() * 10)) # 0 ~ 10 �̸��� ������ ���� ��
print(int(random() * 10) + 1) # 1 ~ 10 ������ ������ ���� ��

print(int(random() * 45) + 1) # 1 ~ 45 ������ ������ ��

print(randrange(1, 46)) # 1 ~ 46 �̸��� ������ ��

print(randint(1, 45)) # 1 ~ 45 ������ ������ ��
