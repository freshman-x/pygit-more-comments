from pygit import read_file
import zlib

path = 'test_repo/.git/objects/dd/c2a5f9d618d10b80e2048c714e5d86a3d705a8'

full_data = zlib.decompress(read_file(path))

print(full_data)

nul_index = full_data.index(b'\x00')
header = full_data[:nul_index]
obj_type, size_str = header.decode().split()
size = int(size_str)
data = full_data[nul_index + 1:]

print(obj_type)
print(size)
# 对应原始的十六进制编码数据，类似于 ‘\xe8\xbf\x99…………’
print(data) 
# 使用 utf-8 解码后的数据，类似于 ‘这…………’
print(data.decode())
