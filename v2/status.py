from enum import Enum

class Status(Enum):

    PASSED = 'Passed'
    FAILED = 'Failed'
    TLE = 'Time Limit Exceeded'
    MLE = 'Memory Limit Exceeded'
    OLE = 'Output Limit Exceeded'
    RUNTIME_ERROR = 'Runtime Error'
    SYNTAX_ERROR = 'Syntax Error'
    SWW = 'Something Went Wrong'