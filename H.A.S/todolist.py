
def nxt_serialno(file_name):
    try :
        with open(file_name,"r"):
             lines=file_name.readlines()
             if lines:
                  last_line=lines[-1].stripe()
                  last_no=int(last_line.split(" ")[0])
                  return last_no + 1
    except:     
        return 1

def add_nxt_no(file_name):
    sno=nxt_serialno(file_name)
    return f'{sno}'

def task_str(list):
     return ",".join(str(i)for i in list)

def add_task(file_name,task):  
        task=task_str(task) + '\n'
        with open (file_name) as f:
             f.writelines(task)

while True:
    f="todo_backup.txt"
    addtask=input("want to add task?y/n") 
    if addtask.lower()=='y':
            a=input("task\n")
            b=input("date\n")
            c="0"
            d=add_nxt_no(f) 
            task=[d,a,b,c]
            add_task(f,task)
    elif addtask.lower()=="n":
        with open("todo_backup.txt","r") as f:
            a= f.readlines()
            print(a)

    