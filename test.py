from filecontentscanner import scanner

x = scanner('test', 'a');
print('All file count:', x.file_count);
print('All folder count:', x.folder_count);
print("Found count:", x.found_count);

for y in x.founds:
    print('Found:', y);
