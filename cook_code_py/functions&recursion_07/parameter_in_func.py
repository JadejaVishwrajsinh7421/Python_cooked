#default parameter
#  -> Assign a default value to paramter when argument is not given


def cal_mul(a=1,b=2):
    print(a*b)
    
cal_mul()#2
cal_mul(2,3)#6
cal_mul(2)#4
cal_mul(1)#2
#we can't pass first param as default then another is non default
