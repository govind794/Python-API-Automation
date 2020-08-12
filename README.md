#REST API Automation Testing

### Install Setup:
- Install [Python3](https://www.python.org/downloads/)
- Install all required packages useing this commend
    ```shell script
       pip install -r requirements.txt 
    ```
  
### Run multiple formate test cases:

- pytest TestRunner/test_Login_Flow.py [run single file test case]
- pytest -m TestRunner/test_Login_Flow.py
- pytest -s -v TestRunner/test_Login_Flow.py