unit-testing目录下的脚本为单元测试脚本，覆盖dolphindbnumpy支持的各种功能。

首先需要在`setup`目录下新建settings.py文件，根据本机的DolphinDB server的配置情况设置所需参数：

```python
HOST = "localhost"
PORT = 8848
WORK_DIR = "/home/root/"
```

执行numpy_testAll.py 文件，将运行当前目录下所有测试文件，并在/tests/reports目录下生成一份名为numpy_unit_report.txt的文件。
