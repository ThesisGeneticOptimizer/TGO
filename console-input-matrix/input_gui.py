import wx
import wx.grid as grid
import csv

currentgrid = 19

class Button(wx.Frame):
    def __init__(self, parent, source):
        wx.Frame.__init__(self, parent, -1, size=(500,500))
        self.source = source
        self.pos = 0 
        self.Show()
        
    

class Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Grid", size=(700,450))
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_OPEN, '&Open')
        menubar.Append(fileMenu, '&File')
        self.Bind(wx.EVT_MENU, self.browse_file, fitem)

        
        self.SetMenuBar(menubar)
        self.grid = grid.Grid(self)
        self.grid.CreateGrid(currentgrid, currentgrid)

    
    def browse_file(self,e):
        with wx.FileDialog(self, "Open CSV file", wildcard="CSV file (*.csv)|*.csv",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind
            
            pathname = fileDialog.GetPath()
            try:
                with open(pathname,newline="") as file:
                    row_count = sum(1 for row in file)
                    print(row_count)
                    self.grid.AppendRows(row_count-currentgrid)
                    self.grid.AppendCols(row_count-currentgrid)
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)
                

        self.display_data(pathname)

    def display_data(self,pathname):
        with open(pathname,newline="") as file:
            reader = csv.reader(file)
            r = 0
            for col in reader:
               c = 0
               for row in col:
                  self.grid.SetCellValue(r,c,row)
                  self.grid.SetCellValue(c,r,row)
                  if row == "":
                      self.grid.SetCellBackgroundColour(r,c,"gray")
                  c += 1
                  
               r += 1
               
            

if __name__ == '__main__':
    app = wx.App(False)
    frame = Frame(None)
    frame.Show()
    app.MainLoop()
