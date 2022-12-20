import os

TEST_DIR = "./src_test"

if __name__ == '__main__':

    testUnits:str = ""

    # 테스트파일만 뽑음
    for (root, directories, files) in os.walk(TEST_DIR):
        for file in files:
            if 'Test.py' in file:
                file_path = os.path.join(root, file)
                testUnits = testUnits + file_path + " "


    syscall = "python3 -m unittest {0}".format(testUnits)
    
    os.system(syscall)