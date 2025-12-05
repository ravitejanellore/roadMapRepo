# provide action and task description
import GBL_operations as GBL

def getId(stmt,action):
    list=stmt.split(' ')
    if action == 'add':
        # if tasks are empty return 0 else return max value among existing ids in tasks dictionary
        id = max([task['id'] for task in tasks]) if tasks else 0
        return id
    elif action == 'update':
        return list[1]
    elif action == 'delete':
        return list[1]
    elif str(action).startswith('mark-'):
        return int(list[1])
      
def addTask(currentId):
    desc=GBL.getTextinsideQuotes(stmt,'"','"')
    tasks.append({'id':int(currentId)+1,'description':desc,'status':'todo'})
    return tasks
def updateTask(id):
    desc=GBL.getTextinsideQuotes(stmt,'"','"')
    taskIndex=GBL.whereContains(int(id),tasks,'id')
    tasks[taskIndex]['description']=desc
    return tasks
def updateStatus(tasks,id,status): 
    taskIndex=GBL.whereContains(id,tasks,'id')
    print(tasks)
    tasks[taskIndex]['status']=status
    return tasks
def deleteTask(id):
    taskIndex=GBL.whereContains(id,tasks,'id')
    print(taskIndex)
    print(tasks[taskIndex])
    tasks.remove(tasks[taskIndex])
    return tasks
def doAction(stmt,action):
    id=getId(stmt,action)
    #default id to zero if None
    id=id if id is not None else 0
    if action=='add':
        return addTask(id)
    elif action=='update':
        return updateTask(id)
    elif action=='delete':
        return deleteTask(int(id))
    elif str(action).startswith('mark-'):
        return updateStatus(tasks,id,action.replace('mark-',''))
file_name = 'my_data.json'
tasks=GBL.readJson(file_name)
tasks=tasks if tasks else []
stmt=str(input('action id description\n'))
action=stmt.split(' ')[0]
tasks=doAction(stmt,action)
GBL.writeJson(file_name,tasks)
print(tasks)





#mark-in-progress 1
#add "Buy Groceries" 
#update 1 "Buy Groceries and veggies"

