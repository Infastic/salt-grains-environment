# salt-grains-environment

My solution to managing what environment my computers are in.

The folder structure here mimics how the file should sit in the [file_root](http://docs.saltstack.com/ref/file_server/file_roots.html).  For example, the *_grains* folder is same *_grains* folder referenced in the [grains doc](http://docs.saltstack.com/topics/targeting/grains.html?highlight=_grains#writing-grains).

##top.sls

This is SaltStack's [top file](http://docs.saltstack.com/ref/states/top.html).  This will show you how to reference the grain created in this repo.
