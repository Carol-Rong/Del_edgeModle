# about katana change tex path

tag_folder = r"root_path/"

all_imageNode_list = NodegraphAPI.GetAllNodesByType("ArnoldShadingNode")
for imageNode in all_imageNode_list:
    if imageNode.getName() == "ArnoldShadingNodebb":
        pass
    else:
        if imageNode.getParameter('nodeType').getValue(0) in ["image", "MayaFile"]:
            image_path = imageNode.getParameter('parameters.filename.value').getValue(0)
            print image_path
            sea_file_path = tag_folder+os.path.basename(image_path)
            #print sea_file_path

            imageNode.getParameter('parameters.filename.value').setValue(sea_file_path, 0)