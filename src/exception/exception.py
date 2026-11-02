import sys              # library to get the info

def error_message_detail(error,error_detail:sys):   # (e,sys)

    _,_,exc_tb = error_detail.exc_info()            # info about the error

    if exc_tb is None:                              # if trabeback is none it will return the actual error
        return f"Error: {error}"

    file_name = exc_tb.tb_frame.f_code.co_filename  #  file name path is obtained 

    line_no = exc_tb.tb_lineno                      # line number of the error

    error_message = (
        f"Error occured at this file [ {file_name} ] at this line [ {line_no} ] and the error is [ {error} ]"
    )

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys=sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )

    def __str__(self):
        return self.error_message

