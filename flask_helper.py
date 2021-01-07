
def ajax_form_to_dict(ajax_request):
    #This function will turn the raw data received from AJAX in a readable dictionary
    ajax_request = str(ajax_request)
    formDict = {}
    #Split all the form elements
    formList = ajax_request.split("&")
    for x in formList:
        #Split the name and value from each form element
        elementList = x.split("=")
        formDict[elementList[0]] = elementList[1]
    return formDict