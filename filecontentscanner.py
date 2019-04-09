# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# NOTE: Created By @bayramlcm
import os
class scanner:
    def __init__(self, folder, content):
        self.file_count = 0;
        self.folder_count = 0;
        self._count(folder);
        self.founds = [];
        self.found_count = 0;
        self.buffer = 1024;
        self._scan(folder, content);
    # NOTE: Dosya içeriğini tara
    def _search(self, path, content):
        length = len(content);
        if length > self.buffer:
            self.buffer = length;
        file = open(path, 'r');
        read = str(file.read(self.buffer));
        before = '';
        while len(read) > 0:
            read = before + read;
            if content in read:
                return True;
            if len(read) > len(content):
                before = content[-len(content):];
            read = str(file.read(self.buffer));
        return False;
    # NOTE: Dosyaları listele
    def _scan(self, path, content):
        info = self._info(path);
        for file in info['file_list']:
            full_path = os.path.join(path, file);
            if self._search(full_path, content):
                self.found_count+=1;
                self.founds.append(full_path);
        for dir in info['folder_list']:
            self._scan(os.path.join(path, dir), content);
    # NOTE: Tüm klasör ve dosyaların toplamı
    def _count(self, path):
        info = self._info(path);
        self.file_count += info['file_count'];
        self.folder_count += info['folder_count'];
        for dir in info['folder_list']:
            self._count(os.path.join(path, dir));
    # NOTE: Klasör ve dosyaları tara
    def _info(self, path):
        folder_count = 0;
        folder_list = [];
        file_count = 0;
        file_list = [];
        for dir in os.listdir(path):
            full_path = os.path.join(path, dir);
            # NOTE: Klasör & Dosya kontrolü
            if os.path.isdir(full_path):
                folder_count += 1;
                folder_list.append(dir);
            elif os.path.isfile(full_path):
                file_count += 1;
                file_list.append(dir);
        return {
            'folder_count': folder_count,
            'folder_list': folder_list,
            'file_count': file_count,
            'file_list': file_list,
        }
