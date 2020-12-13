import sys
import wx
import os
import pdfmergerui
import pdfmerger

class mainmergerui(pdfmergerui.MainFrame):
    """
    docstring
    """
    def guessname(self, event):
        if not self.m_filePicker1.GetPath():
            self.m_filePicker1.SetFocusFromKbd()
            return
        if not self.m_filePicker2.GetPath():
            self.m_filePicker2.SetFocusFromKbd()
            return
        pdf1 = self.m_filePicker1.GetPath()
        if pdf1:
            path = os.path.dirname(pdf1)
            self.m_filePicker3.SetPath(os.path.join(path,'output.pdf'))
        #return super().guessname(event)

    def export(self, event):
        pdf1 = self.m_filePicker1.GetPath()
        pdf2 = self.m_filePicker2.GetPath()
        pdf3 = self.m_filePicker3.GetPath()
        rev1 = self.m_checkBox1.GetValue()
        rev2 = self.m_checkBox2.GetValue()
        mode = self.m_radioBox1.GetSelection()
        if not pdf1:
            self.m_filePicker1.SetFocusFromKbd()
            return
        if not pdf2:
            self.m_filePicker2.SetFocusFromKbd()
            return
        if not pdf3:
            self.m_filePicker3.SetFocusFromKbd()
            return
        #print(pdf1,pdf2,pdf3,rev1,rev2,mode)
        pdfmerger.merge_pdfs(pdf1,rev1,pdf2,rev2,mode,pdf3)
        #return super().export(event)
    pass

if __name__ == "__main__":
    app=wx.App()
    mainui = mainmergerui(None)
    mainui.Show()
    app.MainLoop()
