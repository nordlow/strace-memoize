import inspect

def dln(msg, level_str='info'):

    callerframerecord = inspect.stack()[1]    # 0 represents this line

    # 1 represents line at caller
    frame = callerframerecord[0]

    info = inspect.getframeinfo(frame)

    print(info.filename +       # __FILE__
          ":" +
          str(info.lineno) +    # __LINE__
          ": " +
          level_str + ": ")
