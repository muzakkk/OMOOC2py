#全局引用
+from Tkinter import *
+from ttk import *
+from sys import argv
+reload(sys)
+sys.setdefaultencoding( "utf-8" )
+
+script, filename = argv
+
+#开启窗口
+master = Tk()
+
+#提示信息
+headname = StringVar()
+w = Label(master, textvariable = headname)
+headname.set('编辑' + filename +'.txt')
+w.pack()
+
+#输入框
+v = StringVar()
+e = Entry(master, textvariable = v)
+e.pack()
+
+#通过按钮读取输入的内容，保存到本地文件中
+def callback():
+    txt = v.get()
+    target = open(filename + '.txt', 'a')
+    target.write(txt + '\n')
+    target = open(filename + '.txt')
+    s.set(target.read())
+    e.delete(0, END)
+    e.focus_set()
+
+b = Button(master, text="get", width=10, command=callback)
+b.pack()
+
+#读取文件内容
+s = StringVar()
+target = open(filename + '.txt')
+s.set(target.read())
+#展示文件内容
+w = Message(master, textvariable=s, width=500)
+w.pack()
+
+mainloop() 