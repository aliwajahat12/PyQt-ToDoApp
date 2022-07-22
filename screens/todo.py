from PyQt5.QtCore import QLine
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QLineEdit, QListWidget, \
    QListWidgetItem, QScrollBar


class ToDo(QWidget):
    def __init__(self):
        super(ToDo, self).__init__()
        self.design_layout = QVBoxLayout(self)
        self.setGeometry(800, 200, 1000, 1000)
        self.setWindowTitle("Todo App")
        self.addTaskLabel = None
        self.addTaskTextBox = None
        self.addTaskButton = None
        self.completeTaskButton = None
        self.addTaskText = ""
        self.tasks_list = QListWidget(self)
        self.completed_list = QListWidget(self)
        self.setupUI()

    def addTask(self):
        task = self.addTaskTextBox.text()
        if task != "" and task is not None:
            # self.todoTaskList.append(task)
            # print(self.todoTaskList)
            self.resetTaskLabel()
            QListWidgetItem(task, self.tasks_list)

    def resetTaskLabel(self):
        self.addTaskTextBox.clear()

    def taskCompleted(self):
        if self.tasks_list.currentItem() is not None:
            task = self.tasks_list.currentItem().text()
            self.completed_list.addItem(task)
            self.tasks_list.takeItem(self.tasks_list.row(self.tasks_list.currentItem()))
            self.tasks_list.setCurrentRow(-1)
        elif self.completed_list.currentItem() is not None:
            task = self.completed_list.currentItem().text()
            self.tasks_list.addItem(task)
            self.completed_list.takeItem(self.completed_list.row(self.completed_list.currentItem()))
            self.completed_list.setCurrentRow(-1)

    def setupUI(self):
        add_task_label_row = QHBoxLayout()
        add_task_label_row.totalHeightForWidth(50)

        self.addTaskLabel = QLabel("Add Task", parent=self)
        self.addTaskLabel.setStyleSheet("background-color: lightgrey;"
                                        "border: 1px solid black")
        self.addTaskLabel.setFont(QFont("Times", 13, QFont.Bold))

        add_task_label_row.addWidget(self.addTaskLabel)

        add_task_textbox_row = QHBoxLayout()

        self.addTaskTextBox = QLineEdit(self)

        self.addTaskButton = QPushButton("Add Task", parent=self)
        self.addTaskButton.clicked.connect(self.addTask)
        self.addTaskButton.setObjectName("AddTaskButton")
        self.addTaskButton.setStyleSheet("QPushButton:hover"
                                         "{"
                                         "background-color:lightgreen;"
                                         "}"
                                         "QPushButton"
                                         "{"
                                         "background-color: lightblue"
                                         "}"
                                         )
        self.addTaskButton.setFont(QFont("Open Sans", 10))

        add_task_textbox_row.addWidget(self.addTaskTextBox)
        add_task_textbox_row.addWidget(self.addTaskButton)

        tasks_list_label_row = QHBoxLayout()

        tasks_label = QLabel("Pending Tasks", parent=self)
        tasks_label.setStyleSheet("background-color: lightgrey;"
                                  "border: 1px solid black")
        tasks_label.setFont(QFont("Times", 13, QFont.Bold))

        tasks_list_label_row.addWidget(tasks_label)

        tasks_list_row = QHBoxLayout()

        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet("background: lightgrey;")

        self.tasks_list.setVerticalScrollBar(scroll_bar)
        self.tasks_list.setSpacing(5)
        self.tasks_list.setFont(QFont("Open Sans", 10))
        tasks_list_row.addWidget(self.tasks_list)

        complete_task_button_row = QHBoxLayout()

        self.completeTaskButton = QPushButton("Mark Task As Complete / Pending")
        self.completeTaskButton.clicked.connect(self.taskCompleted)
        self.completeTaskButton.setObjectName("AddTaskButton")
        self.completeTaskButton.setStyleSheet("QPushButton:hover"
                                              "{"
                                              "background-color:purple;"
                                              "}"
                                              "QPushButton"
                                              "{"
                                              "background-color: blue;"
                                              "color: white;"
                                              "}"
                                              )
        self.completeTaskButton.setFont(QFont("Open Sans", 12))

        complete_task_button_row.addWidget(self.completeTaskButton)

        completed_tasks_list_label_row = QHBoxLayout()

        completed_tasks_label = QLabel("Completed Tasks", parent=self)
        completed_tasks_label.setStyleSheet("background-color: lightgrey;"
                                            "border: 1px solid black")
        completed_tasks_label.setFont(QFont("Times", 13, QFont.Bold))

        completed_tasks_list_label_row.addWidget(completed_tasks_label)

        completed_tasks_list_row = QHBoxLayout()

        completed_scroll_bar = QScrollBar()
        completed_scroll_bar.setStyleSheet("background: lightgrey;")

        self.completed_list.setVerticalScrollBar(completed_scroll_bar)
        self.completed_list.setSpacing(5)
        self.completed_list.setFont(QFont("Open Sans", 10))
        completed_tasks_list_row.addWidget(self.completed_list)

        self.design_layout.addLayout(add_task_label_row)
        self.design_layout.addLayout(add_task_textbox_row)
        self.design_layout.addLayout(tasks_list_label_row)
        self.design_layout.addLayout(tasks_list_row)
        self.design_layout.addLayout(complete_task_button_row)
        self.design_layout.addLayout(completed_tasks_list_label_row)
        self.design_layout.addLayout(completed_tasks_list_row)
        self.setLayout(self.design_layout)
