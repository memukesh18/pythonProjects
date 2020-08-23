import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('./Files/errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
    

try:
    errorFile = open('Files/errorInfo.txt', 'r')
    errContent = errorFile.read()
    print(errContent)
    errorFile.close()
except:
    print('Exception Occured.')
