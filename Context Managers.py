from contextlib import contextmanager

@contextmanager

def open_file(file,mode):
    f = open(file, mode)
    yield f
    f.close()

with open_file("sampl2.txt", "w") as f:
    f.write("Good Morning")

print(f.close)


# class Open_File():
#
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# with Open_File("Rober.txt","w") as f:
#     f.write("TEST")
#
# print(f.closed)