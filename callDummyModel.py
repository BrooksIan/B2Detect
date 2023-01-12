flowFileList = session.get(100)
if not flowFileList.isEmpty():
	for flowFile in flowFileList: 
		newFlowFile = session.create(flowFile) 
          
	if (newFlowFile != None):
		newFlowFile = session.putAttribute(newFlowFile, 'confidence', '99.99')
        
	if(errorOccurred){session.transfer(flowFile, REL_FAILURE)}
	
	else{session.transfer(flowFile, REL_SUCCESS)}	
