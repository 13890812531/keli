import os
import pytest
if __name__ == '__main__':
    # pytest.main(["-vs"])
    pytest.main(["-vs","--alluredir","./temp","--clean-alluredir"])
    os.system("allure generate ./temp -o ./report --clean")