

import tkinter
import tkinter.messagebox

def main():
    flag = True;

    def change_label_text():
        nonlocal flag
        flag = not flag;
        color, msg = ('red', 'hello world') if flag else ('blue', 'goodbye world' );
        label.config( text=msg,fg=color);

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('warnning','Quit'):
            top.quit();

    #创建顶层窗口
    top = tkinter.Tk();
    #设置窗口大小
    top.geometry('240x160');
    #设置窗口标题
    top.title('windos title');
    #创建标签并添加到顶层窗口
    label = tkinter.Label(top,text='HelloWorld!', font='Arial -32', fg='red');
    label.pack(expand=1);
    #创建一个装按钮的容器
    panel = tkinter.Frame(top);
    #创建按钮
    button1 = tkinter.Button(panel,text='modify', command=change_label_text);
    button1.pack(side='left');

    button2 = tkinter.Button(panel,text='exit',command=confirm_to_quit);
    button2.pack(side='right');

    panel.pack(side='bottom');

    #主事件循环
    tkinter.mainloop();

if __name__ == '__main__':
    main();
    
