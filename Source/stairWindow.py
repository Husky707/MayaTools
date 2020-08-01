from PySide2 import QtWidgets, QtCore
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
import spiralStairs

def maya_main_window():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class StairWindow(QtWidgets.QDialog):

    def __init__(self):
        super(StairWindow, self).__init__(parent = maya_main_window())
        self.setWindowTitle('Spiral Stair Maker')
        self.resize(140, 200)
        self.core = spiralStairs.Stairs()

        self.create_widgets()
        self.create_layout()



    def create_widgets(self):
        self.lbl_title = QtWidgets.QLabel("Spiral Stair Creator")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")
        self.btn_build = QtWidgets.QPushButton("Build")

        self.create_step_widgets()
        self.create_height_widgets()
        self.create_connections()

    def create_layout(self):
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addWidget(self.lbl_title)
        self.setLayout(self.mainLayout)

        self.layout_step_editor()
        self.layout_height_editor()

        self.lay_end = QtWidgets.QHBoxLayout()
        self.lay_end.addWidget(self.btn_cancel)
        self.lay_end.addWidget(self.btn_build)

        self.mainLayout.addStretch()
        self.mainLayout.addLayout(self.lay_end)

    def create_step_widgets(self):
        self.lbl_length = QtWidgets.QLabel("Length")
        self.lbl_height = QtWidgets.QLabel("Height")
        self.lbl_depth = QtWidgets.QLabel("Depth")
        self.lbl_angle = QtWidgets.QLabel("Angle")

        self.ln_length = QtWidgets.QSpinBox()
        self.ln_length.setValue(3)
        self.ln_length.setMinimum(1)
        self.ln_height = QtWidgets.QSpinBox()
        self.ln_height.setValue(2)
        self.ln_height.setMinimum(1)
        self.ln_depth = QtWidgets.QSpinBox()
        self.ln_depth.setValue(1)
        self.ln_depth.setMinimum(1)
        self.ln_angle = QtWidgets.QSpinBox()
        self.ln_angle.setValue(15)
        self.ln_angle.setMinimum(1)

    def create_height_widgets(self):
        self.lbl_maxSteps = QtWidgets.QLabel("Max Steps")
        self.lbl_maxHeight= QtWidgets.QLabel("Max Height")
        self.chk_mode = QtWidgets.QCheckBox("Limit Height By Steps")
        self.chk_mode.setChecked(True)

        self.ln_maxSteps = QtWidgets.QSpinBox()
        self.ln_maxSteps.setValue(6)
        self.ln_maxSteps.setMinimum(1)
        self.ln_maxHeight = QtWidgets.QSpinBox()
        self.ln_maxHeight.setValue(12)
        self.ln_maxHeight.setMinimum(1)

    def layout_height_editor(self):
        self.lay_height_editor = QtWidgets.QHBoxLayout()

        self.lay_maxSteps = QtWidgets.QVBoxLayout()
        self.lay_maxSteps.addWidget(self.lbl_maxSteps)
        self.lay_maxSteps.addWidget(self.ln_maxSteps)
        self.lay_height_editor.addLayout(self.lay_maxSteps)

        self.lay_maxHeight = QtWidgets.QVBoxLayout()
        self.lay_maxHeight.addWidget(self.lbl_maxHeight)
        self.lay_maxHeight.addWidget(self.ln_maxHeight)
        self.lay_height_editor.addLayout(self.lay_maxHeight)

        self.mainLayout.addWidget(self.chk_mode)
        self.mainLayout.addLayout(self.lay_height_editor)

    def layout_step_editor(self):
        self.lay_steps = QtWidgets.QVBoxLayout()

        self.lay_length = QtWidgets.QHBoxLayout()
        self.lay_length.addWidget(self.lbl_length)
        self.lay_length.addWidget(self.ln_length)
        self.lay_steps.addLayout(self.lay_length)

        self.lay_height = QtWidgets.QHBoxLayout()
        self.lay_height.addWidget(self.lbl_height)
        self.lay_height.addWidget(self.ln_height)
        self.lay_steps.addLayout(self.lay_height)

        self.lay_depth = QtWidgets.QHBoxLayout()
        self.lay_depth.addWidget(self.lbl_depth)
        self.lay_depth.addWidget(self.ln_depth)
        self.lay_steps.addLayout(self.lay_depth)

        self.lay_angle = QtWidgets.QHBoxLayout()
        self.lay_angle.addWidget(self.lbl_angle)
        self.lay_angle.addWidget(self.ln_angle)
        self.lay_steps.addLayout(self.lay_angle)

        self.mainLayout.addLayout(self.lay_steps)

    def create_connections(self):
        self.btn_cancel.clicked.connect(self.onCancel)
        self.btn_build.clicked.connect(self.onBuild)

        self.chk_mode.stateChanged.connect(self.onChangeMode)
        self.ln_maxSteps.valueChanged.connect(self.onSetStairCap)
        self.ln_maxHeight.valueChanged.connect(self.onSetHeightCap)

        self.ln_angle.valueChanged.connect(self.onStepAngle)
        self.ln_height.valueChanged.connect(self.onStepHeight)
        self.ln_length.valueChanged.connect(self.onStepWidth)
        self.ln_depth.valueChanged.connect(self.onStepDepth)

    def onCancel(self):
        self.core.delete_stairs()
        self.close()

    def onBuild(self):
        self.self.close()

    def onStepHeight(self, val):
        self.core.set_step_height(val)

    def onStepDepth(self, val):
        self.core.set_step_depth(val)

    def onStepWidth(self, val):
        self.core.set_step_width(val)

    def onStepAngle(self, val):
        self.core.set_step_rotation(val)

    def onChangeMode(self, state):
        self.core.set_height_cap_mode(state)

    def onSetStairCap(self, val):
        self.core.set_stair_cap(val)

    def onSetHeightCap(self, val):
        self.core.set_height_cap(val)





















