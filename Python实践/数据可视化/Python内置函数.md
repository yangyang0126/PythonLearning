# [内置函数](https://docs.python.org/zh-cn/3.7/library/functions.html#any)

根据官网内容整理

Python 解释器内置了很多函数和类型，您可以在任何时候使用它们。以下按字母表顺序列出它们。

|                                                              |                                                              |                                                              |                                                              |                                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | ------------------------------------------------------------ |
| [`abs()`](https://docs.python.org/zh-cn/3.7/library/functions.html#abs) | [`delattr()`](https://docs.python.org/zh-cn/3.7/library/functions.html#delattr) | [`hash()`](https://docs.python.org/zh-cn/3.7/library/functions.html#hash) | [`memoryview()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-memoryview) | [`set()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-set) |
| [`all()`](https://docs.python.org/zh-cn/3.7/library/functions.html#all) | [`dict()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-dict) | [`help()`](https://docs.python.org/zh-cn/3.7/library/functions.html#help) | [`min()`](https://docs.python.org/zh-cn/3.7/library/functions.html#min) | [`setattr()`](https://docs.python.org/zh-cn/3.7/library/functions.html#setattr) |
| [`any()`](https://docs.python.org/zh-cn/3.7/library/functions.html#any) | [`dir()`](https://docs.python.org/zh-cn/3.7/library/functions.html#dir) | [`hex()`](https://docs.python.org/zh-cn/3.7/library/functions.html#hex) | [`next()`](https://docs.python.org/zh-cn/3.7/library/functions.html#next) | [`slice()`](https://docs.python.org/zh-cn/3.7/library/functions.html#slice) |
| [`ascii()`](https://docs.python.org/zh-cn/3.7/library/functions.html#ascii) | [`divmod()`](https://docs.python.org/zh-cn/3.7/library/functions.html#divmod) | [`id()`](https://docs.python.org/zh-cn/3.7/library/functions.html#id) | [`object()`](https://docs.python.org/zh-cn/3.7/library/functions.html#object) | [`sorted()`](https://docs.python.org/zh-cn/3.7/library/functions.html#sorted) |
| [`bin()`](https://docs.python.org/zh-cn/3.7/library/functions.html#bin) | [`enumerate()`](https://docs.python.org/zh-cn/3.7/library/functions.html#enumerate) | [`input()`](https://docs.python.org/zh-cn/3.7/library/functions.html#input) | [`oct()`](https://docs.python.org/zh-cn/3.7/library/functions.html#oct) | [`staticmethod()`](https://docs.python.org/zh-cn/3.7/library/functions.html#staticmethod) |
| [`bool()`](https://docs.python.org/zh-cn/3.7/library/functions.html#bool) | [`eval()`](https://docs.python.org/zh-cn/3.7/library/functions.html#eval) | [`int()`](https://docs.python.org/zh-cn/3.7/library/functions.html#int) | [`open()`](https://docs.python.org/zh-cn/3.7/library/functions.html#open) | [`str()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-str) |
| [`breakpoint()`](https://docs.python.org/zh-cn/3.7/library/functions.html#breakpoint) | [`exec()`](https://docs.python.org/zh-cn/3.7/library/functions.html#exec) | [`isinstance()`](https://docs.python.org/zh-cn/3.7/library/functions.html#isinstance) | [`ord()`](https://docs.python.org/zh-cn/3.7/library/functions.html#ord) | [`sum()`](https://docs.python.org/zh-cn/3.7/library/functions.html#sum) |
| [`bytearray()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-bytearray) | [`filter()`](https://docs.python.org/zh-cn/3.7/library/functions.html#filter) | [`issubclass()`](https://docs.python.org/zh-cn/3.7/library/functions.html#issubclass) | [`pow()`](https://docs.python.org/zh-cn/3.7/library/functions.html#pow) | [`super()`](https://docs.python.org/zh-cn/3.7/library/functions.html#super) |
| [`bytes()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-bytes) | [`float()`](https://docs.python.org/zh-cn/3.7/library/functions.html#float) | [`iter()`](https://docs.python.org/zh-cn/3.7/library/functions.html#iter) | [`print()`](https://docs.python.org/zh-cn/3.7/library/functions.html#print) | [`tuple()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-tuple) |
| [`callable()`](https://docs.python.org/zh-cn/3.7/library/functions.html#callable) | [`format()`](https://docs.python.org/zh-cn/3.7/library/functions.html#format) | [`len()`](https://docs.python.org/zh-cn/3.7/library/functions.html#len) | [`property()`](https://docs.python.org/zh-cn/3.7/library/functions.html#property) | [`type()`](https://docs.python.org/zh-cn/3.7/library/functions.html#type) |
| [`chr()`](https://docs.python.org/zh-cn/3.7/library/functions.html#chr) | [`frozenset()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-frozenset) | [`list()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-list) | [`range()`](https://docs.python.org/zh-cn/3.7/library/functions.html#func-range) | [`vars()`](https://docs.python.org/zh-cn/3.7/library/functions.html#vars) |
| [`classmethod()`](https://docs.python.org/zh-cn/3.7/library/functions.html#classmethod) | [`getattr()`](https://docs.python.org/zh-cn/3.7/library/functions.html#getattr) | [`locals()`](https://docs.python.org/zh-cn/3.7/library/functions.html#locals) | [`repr()`](https://docs.python.org/zh-cn/3.7/library/functions.html#repr) | [`zip()`](https://docs.python.org/zh-cn/3.7/library/functions.html#zip) |
| [`compile()`](https://docs.python.org/zh-cn/3.7/library/functions.html#compile) | [`globals()`](https://docs.python.org/zh-cn/3.7/library/functions.html#globals) | [`map()`](https://docs.python.org/zh-cn/3.7/library/functions.html#map) | [`reversed()`](https://docs.python.org/zh-cn/3.7/library/functions.html#reversed) | [`__import__()`](https://docs.python.org/zh-cn/3.7/library/functions.html#__import__) |
| [`complex()`](https://docs.python.org/zh-cn/3.7/library/functions.html#complex) | [`hasattr()`](https://docs.python.org/zh-cn/3.7/library/functions.html#hasattr) | [`max()`](https://docs.python.org/zh-cn/3.7/library/functions.html#max) | [`round()`](https://docs.python.org/zh-cn/3.7/library/functions.html#round) |                                                              |



`abs`(*x*)：返回一个数的绝对值

```python
abs(5)
# 输出： 5
abs(-5.1)
# 输出： 5.1
abs(complex(3,4))
# 输出： 5.0
```

`ascii`(*object*)：返回一个对象可打印的字符串

```python
ascii('你的名字是ABC')  
# 输出： "'\\u4f60\\u7684\\u540d\\u5b57\\u662fABC'"
```

`bin`(*x*)：将一个整数转变为一个前缀为“0b”的二进制字符串

