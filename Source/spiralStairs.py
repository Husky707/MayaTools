import pymel.core as pm

class Stairs(object):


    def __init__(self):
        self.numStairs = 0
        self.strWidth = 3.0
        self.strDepth = 2.0
        self._strHeight = 1.0
        self.strRo = 15

        self.limitHeightBySteps = True
        self.heightCap = 12
        self.stairCap = 6

        self._stairs = []
        self.add_stairs(6)

    @property
    def strHeight(self):
        return self._strHeight
    @strHeight.setter
    def strHeight(self, newHeight):
        self._strHeight = newHeight
        if(self.limitHeightBySteps == False):
            while((newHeight * self.numStairs) > self.heightCap):
                self._remove_stair()

    def _remove_stair(self):
        self._stairs.pop(-1)
        self.numStairs = self.numStairs - 1
        """Can you really not use '--'????"""

        pm.delete(self._index_to_name(self.numStairs))

    def delete_stairs(self):
        num = self.numStairs
        for index in range(num):
            self._remove_stair()

    def add_stairs(self, num):
        curCount = len(self._stairs)
        namePattern = "{obj}{num}"
        print("Tried to add stairs")

        for index in range(num):
            if(self._can_increase_height == False):
                return
            name = namePattern.format(obj = 'step', num = curCount + index)
            self._stairs.append(pm.polyCube(n = name ))
            self._build_step(name)
            self._set_step_pivot(name)
            self._rotate_step(name, curCount + index)
            self._set_step_altitude(name, curCount + index)
            self.numStairs = self.numStairs + 1

    def _can_increase_height(self):
        if self.limitHeightBySteps:
            return self.numStairs < self.stairCap
        else:
            return (self.numStairs + 1) * self._strHeight < self.heightCap

    def set_step_depth(self, depth):
        self.strDepth = depth + self.strDepth
        for index in range(self.numStairs):
            pm.select(self._index_to_name(index) + '.f[2]')
            pm.scale(self.strDepth, z=True)

    def set_step_width(self, width):
        self.strWidth = width + self.strWidth
        for index in range(self.numStairs):
            pm.select(self._index_to_name(index) + '.f[4]')
            pm.move(self.strWidth, x=True)

    def set_step_height(self, height):
        self._strHeight = height + self._strHeight
        for index in range(self.numStairs):
            name = self._index_to_name(index)
            pm.select(name + '.f[1]')
            pm.scale(self.strHeight, y=True)
            self._set_step_altitude(name, index)

    def set_step_rotation(self, rotation):
        deltaRo = rotation - self.strRo
        self.strRo = rotation + self.strRo
        for index in range(self.numStairs):
            pm.rotate(self._index_to_name(index), self.strRo * index, y=True)

    def set_height_cap_mode(self, bool):
        """setting to true limits the hight by a number of steps"""
        if bool:
            while self.numStairs > self.stairCap:
                self._remove_stair()
        else:
            while ((self._strHeight * self.numStairs) > self.heightCap):
                self._remove_stair()

        self.limitHeightBySteps = bool

    def set_stair_cap(self, num):
        deltaCap = num - self.stairCap
        self.stairCap = num
        if(self.limitHeightBySteps & deltaCap < 0):
            while self.numStairs < self.stairCap:
                self._remove_stair()

    def set_height_cap(self, max):
        deltaMax = max - self.heightCap
        self.heightCap = max
        if(self.limitHeightBySteps == False & deltaMax < 0):
            while (self.numStairs * self._strHeight > self.heightCap):
                self._remove_stair()

    def _build_step(self, objName):
        pm.select(objName + '.f[4]')
        pm.move(self.strWidth, x=True)
        pm.select(objName + '.f[1]')
        pm.scale(self.strHeight, y=True)
        pm.select(objName + '.f[2]')
        pm.scale(self.strDepth, z=True)

    def _set_step_pivot(self, objName):
        pm.select(objName + '.f[5]')
        pm.move(0, x=True)
        pm.select(objName + '.f[3]')
        pm.scale(0, y=True)
        pm.select(objName + '.f[0]')
        pm.scale(0, z=True)

    def _rotate_step(self, objName, iStep):
        pm.rotate(objName, iStep * self.strRo, y=True)

    def _set_step_altitude(self, objName, iStep):
        pm.move(objName, (self._strHeight * iStep)/2.0, y=True)



    def _index_to_name(self, i):
        namePattern = "{obj}{num}"
        name = namePattern.format(obj='step', num=i)
        return name
