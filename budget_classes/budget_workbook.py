from openpyxl.workbook.workbook import (Workbook,
                                        ReadOnlyWorkbookException,
                                        WriteOnlyWorksheet)

from budget_classes.budget_worksheet import BudgetWorksheet


class BudgetWorkbook(Workbook):

    def create_sheet(self, title=None, index=None):
        """Create a worksheet (at an optional index).

        :param title: optional title of the sheet
        :type title: str
        :param index: optional position at which the sheet will be inserted
        :type index: int

        """
        if self.read_only:
            raise ReadOnlyWorkbookException('Cannot create new sheet in a read-only workbook')

        if self.write_only:
            new_ws = WriteOnlyWorksheet(parent=self, title=title)
        else:
            new_ws = BudgetWorksheet(parent=self, title=title)

        self._add_sheet(sheet=new_ws, index=index)
        return new_ws

    def initialize_budget_workbook(self):
        active = self.active
        self.create_sheet('Expenses')
        self.create_sheet('Income')
        self.create_sheet('Balance')
        self.create_sheet('Control')
        self.remove_sheet(active)

        self.save('./wb_budget.xlsx')