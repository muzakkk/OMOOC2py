#ȫ������
+from Tkinter import *
+from ttk import *
+from sys import argv
+reload(sys)
+sys.setdefaultencoding( "utf-8" )
+
+script, filename = argv
+
+#��������
+master = Tk()
+
+#��ʾ��Ϣ
+headname = StringVar()
+w = Label(master, textvariable = headname)
+headname.set('�༭' + filename +'.txt')
+w.pack()
+
+#�����
+v = StringVar()
+e = Entry(master, textvariable = v)
+e.pack()
+
+#ͨ����ť��ȡ��������ݣ����浽�����ļ���
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
+#��ȡ�ļ�����
+s = StringVar()
+target = open(filename + '.txt')
+s.set(target.read())
+#չʾ�ļ�����
+w = Message(master, textvariable=s, width=500)
+w.pack()
+
+mainloop() 