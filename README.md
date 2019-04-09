# filecontentscanner
File content scanner with Python 2.x or Python 3.x<br/>
Stable and fast scanner<br/>
# example
<code>from filecontentscanner import scanner;</code><br/>
<code>fs = scanner('folder', 'keyword');</code><br/>
Total files count: <code>fs.file_count</code><br/>
Total folders count: <code>fs.folder_count</code><br/>
Total founds count: <code>fs.found_count</code><br/>
Founds: <code>fs.founds</code>
<pre>
for file in x.founds:
    print('Found:', file);
</pre>

<a href="http://www.bayramlcm.com/" target="_blank">@bayramlcm</a>
