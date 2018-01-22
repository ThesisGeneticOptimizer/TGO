import wx
import wx.grid as grid
import csv

# Define the tab content as classes:
currentgrid = 19

tab_array1 = []
tab_array2 = []
tab_array3 = []
tab_array4 = []
tab_array5 = []
tab_array6 = []
tab_array7 = []


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="", size=(700,450))

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_SAVE, '&Save')
        menubar.Append(fileMenu, '&File')
        self.Bind(wx.EVT_MENU, self.save_data, fitem)
        self.SetMenuBar(menubar)
        
 
        # Create a panel and notebook (tabs holder)
        p = wx.Panel(self)
        nb = wx.Notebook(p)
 
        # Create the tab windows
        tab1 = TabOne(nb)
        tab2 = TabTwo(nb)
        tab3 = TabThree(nb)
        tab4 = TabFour(nb)
        tab5 = TabFive(nb)
        tab6 = TabSix(nb)
        tab7 = TabSeven(nb)

 
        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "No Relationship")
        nb.AddPage(tab2, "Friends")
        nb.AddPage(tab3, "Aunt/Niece")
        nb.AddPage(tab4, "Cousin")
        nb.AddPage(tab5, "Parent/child")
        nb.AddPage(tab6, "Sibling")
        nb.AddPage(tab7, "Spouse Date")

        
        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)
    
    def save_data(self,e):
        print(tab_array1)
        print(tab_array2)
        print(tab_array3)
        print(tab_array4)
        print(tab_array5)
        print(tab_array6)
        print(tab_array7)

class TabOne(wx.Panel,MainFrame):
    global oldval
    oldval = ""
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "No relationship", (20,20))
        self.grid = grid.Grid(self,size=(700,450))
        self.grid.CreateGrid(currentgrid, currentgrid)
        self.grid.Bind(grid.EVT_GRID_CELL_CHANGED, self.OnCellChange)

    def OnCellChange(self, evt):
        print("OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition()))

        row = evt.GetRow()
        col = evt.GetCol()
        val = self.grid.GetCellValue(row, col)
        #print(row,col)
        
        if len(tab_array1) != 0:
            if tab_array1[row-1] != val:
                tab_array1[row] = val
            else:
                tab_array1.append(val)
        else:
            tab_array1.append(val)


    
class TabTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "No relationship", (20,20))
        self.grid = grid.Grid(self,size=(700,450))
        self.grid.CreateGrid(currentgrid, currentgrid)
        self.grid.Bind(grid.EVT_GRID_CELL_CHANGED, self.OnCellChange)

    def OnCellChange(self, evt):
        print("OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition()))

        row = evt.GetRow()
        col = evt.GetCol()
        val = self.grid.GetCellValue(row, col)

        if len(tab_array2) != 0:
            if tab_array2[row-1] != val:
                tab_array2[row] = val
            else:
                tab_array2.append(val)
        else:
            tab_array2.append(val)
            
class TabThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "No relationship", (20,20))
        self.grid = grid.Grid(self,size=(700,450))
        self.grid.CreateGrid(currentgrid, currentgrid)
        self.grid.Bind(grid.EVT_GRID_CELL_CHANGED, self.OnCellChange)

    def OnCellChange(self, evt):
        print("OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition()))

        row = evt.GetRow()
        col = evt.GetCol()
        val = self.grid.GetCellValue(row, col)

        if len(tab_array1) != 0:
            if tab_array3[row-1] != val:
                tab_array3[row] = val
            else:
                tab_array3.append(val)
        else:
            tab_array3.append(val)
            
class TabFour(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "No relationship", (20,20))
        self.grid = grid.Grid(self,size=(700,450))
        self.grid.CreateGrid(currentgrid, currentgrid)
        self.grid.Bind(grid.EVT_GRID_CELL_CHANGED, self.OnCellChange)

    def OnCellChange(self, evt):
        print("OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition()))

        row = evt.GetRow()
        col = evt.GetCol()
        val = self.grid.GetCellValue(row, col)

        if len(tab_array4) != 0:
            if tab_array4[row-1] != val:
                tab_array4[row] = val
            else:
                tab_array4.append(val)
        else:
            tab_array4.append(val)
            
class TabFive(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "No relationship", (20,20))
        self.grid = grid.Grid(self,size=(700,450))
        self.grid.CreateGrid(currentgrid, currentgrid)
        self.grid.Bind(grid.EVT_GRID_CELL_CHANGED, self.OnCellChange)

    def OnCellChange(self, evt):
        print("OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition()))

        row = evt.GetRow()
        col = evt.GetCol()
        val = self.grid.GetCellValue(row, col)

        if len(tab_array5) != 0:
            if tab_array5[row-1] != val:
                tab_array5[row] = val
            else:
                tab_array5.append(val)
        else:
            tab_array5.append(val)
class TabSix(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "No relationship", (20,20))
        self.grid = grid.Grid(self,size=(700,450))
        self.grid.CreateGrid(currentgrid, currentgrid)
        self.grid.Bind(grid.EVT_GRID_CELL_CHANGED, self.OnCellChange)

    def OnCellChange(self, evt):
        print("OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition()))

        row = evt.GetRow()
        col = evt.GetCol()
        val = self.grid.GetCellValue(row, col)

        if len(tab_array6) != 0:
            if tab_array6[row-1] != val:
                tab_array6[row] = val
            else:
                tab_array6.append(val)
        else:
            tab_array6.append(val)
class TabSeven(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "No relationship", (20,20))
        self.grid = grid.Grid(self,size=(700,450))
        self.grid.CreateGrid(currentgrid, currentgrid)
        self.grid.Bind(grid.EVT_GRID_CELL_CHANGED, self.OnCellChange)

    def OnCellChange(self, evt):
        print("OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition()))

        row = evt.GetRow()
        col = evt.GetCol()
        val = self.grid.GetCellValue(row, col)

        if len(tab_array7) != 0:
            if tab_array7[row-1] != val:
                tab_array7[row] = val
            else:
                tab_array7.append(val)
        else:
            tab_array7.append(val)
 
if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
