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

def del_line(set_name,del_attr,base_list):
    model_list = cmds.sets(set_name,q=True)
    for model_name in model_list:
        tag_list = []
        for key in base_list:
            ele = model_name+'.'+del_attr+'['+str(key)+']'
            tag_list.append(ele)
        cmds.polyDelEdge(tag_list,cv=True,ch=True)

def remove_select():
    new_set_name = cmds.textField('new_setName',q=True,text=True)  
    sel_model = cmds.ls(sl=True)
    for key in sel_model:
        set_nemeList = cmds.listSets(object = key)
        if len(set_nemeList) == 2:
            for name in set_nemeList:
                if name is not "modelPanel4ViewSelectedSet":
                    set_name = name
                    cmds.sets(key,rm=set_name)              
        elif len(set_nemeList) > 2:
            cmds.warning('Please check the set for the selected object!')    
    cmds.sets(sel_model,n=new_set_name)

def unit_delLine():
    sel_lines = cmds.ls(sl=True)
    sel_allLines = []
    for key in sel_lines:
        model_num = key.split('.')
        del_attr = model_num[1].split('[')    
        line_num = del_attr[1].split(']')
        sel_allLines.append(line_num[0])
    set_list = cmds.listSets(object = model_num[0])
    if len(set_list) == 2:
        for key in set_list:
            if key is not "modelPanel4ViewSelectedSet":
                set_name = key
    elif len(set_list) > 2:
        cmds.warning('Please check the set for the selected object!')
    del_line(set_name,del_attr[0],sel_allLines)    

def ui():
    if cmds.window("Del_line",exists=True):
        cmds.deleteUI("Del_line")
    
    cmds.window("Del_line")
    cmds.columnLayout()
    cmds.rowLayout(numberOfColumns=2)
    cmds.separator( w=140,h=5, style='none' )
    cmds.button('Create Set',c='sort_set()',w=70)
    cmds.setParent('..')    
    cmds.rowLayout(numberOfColumns=2)
    cmds.separator( w=140,h=5, style='none' )   
    cmds.button('Delete Edge',c='unit_delLine()',w=70)
    cmds.setParent('..')   
    cmds.rowLayout(numberOfColumns=4)
    cmds.separator( w=140,h=5, style='none' )
    cmds.text('New Set Name:')
    cmds.textField('new_setName')
    cmds.button('Remove Select',c='remove_select()')
    cmds.setParent('..')
    
    cmds.setParent('..')
    cmds.showWindow("Del_line")
       
ui()
    