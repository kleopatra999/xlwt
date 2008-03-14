# -*- coding: windows-1252 -*-

# 2007-01-14 SJM Added assertions on type & range of column index; removed @accepts
# 2007-01-10 SJM Added set_style() method


from BIFFRecords import ColInfoRecord

class Column(object):
    def __init__(self, colx, parent_sheet):
        if not(isinstance(colx, int) and 0 <= colx <= 255):
            raise ValueError("column index (%r) not an int in range(256)" % colx)
        self._index = colx
        self._parent = parent_sheet
        self._parent_wb = parent_sheet.get_parent()
        self._xf_index = 0x0F

        self.width = 0x0B92
        self.hidden = 0
        self.level = 0
        self.collapse = 0

    def set_style(self, style):
        self._xf_index = self._parent_wb.add_style(style)

    def get_biff_record(self):
        options =  (self.hidden & 0x01) << 0
        options |= (self.level & 0x07) << 8
        options |= (self.collapse & 0x01) << 12
        
        return ColInfoRecord(self._index, self._index, self.width, self._xf_index, options).get()
        
        
        
