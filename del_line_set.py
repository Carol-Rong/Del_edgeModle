import maya.cmds as cmds

golbal_dict = {8:[],11:[],16:[],20:[],24:[],27:[],28:[],32:[],36:[],40:[],44:[],60:[],68:[],72:[]}

def nums_face(sel_name,nums):    
    for key in golbal_dict:
        if nums == key:
            golbal_dict[nums].append(sel_name)
               
def sort_model():
    sel_face = cmds.ls(sl=True)[0]
    all_list = cmds.listRelatives(sel_face,children=True)
    for model_name in all_list:
        nums = cmds.polyEvaluate(model_name,face=True)
        nums_face(model_name,nums)
    return golbal_dict
    
def sort_set():
    new_dict = sort_model()
    for key in new_dict:
        cmds.sets(new_dict[key],n='mao_faceNum_'+str(key))


def del_line(set_name,base_list):
    model_list = cmds.sets(set_name,q=True)
    for model_name in model_list:
        tag_list = []
        for key in base_list:
            ele = model_name+'.e[' + str(key)+']'
            tag_list.append(ele)
        cmds.polyDelEdge(tag_list,cv=True,ch=True)
             
def unit():                    
    sel_str = cmds.textField('sel_str',q=True,text=True)
    sel_list = sel_str.split(',')
    set_name = cmds.textField('set_name',q=True,text=True)
    del_line(set_name,sel_list)

def ui():
    if cmds.window("Del_line",exists=True):
        cmds.deleteUI("Del_line")
    
    cmds.window("Del_line")
    cmds.columnLayout()
    cmds.button('Create Set',c='sort_set()')
    cmds.rowLayout(numberOfColumns=2)
    cmds.text('Line Numbers:')
    cmds.textField('sel_str')
    cmds.setParent('..')
    
    cmds.rowLayout(numberOfColumns=3)
    cmds.text('set_name:')
    cmds.textField('set_name')
    cmds.button('del_line',c='unit()')    
    cmds.setParent('..')
    
    cmds.setParent('..')
    cmds.showWindow("Del_line")
       
ui()


    