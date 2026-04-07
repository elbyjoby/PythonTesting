# This is a sample Python script.
from unittest import result

from axis_bank import AxisBankaccount
from hdfc_bank import HdfcBankaccount
# from axis_bank import AxisBankaccount
# from hdfc_bank import HdfcBankaccount
from rbi_bank import RbiBank
from society import Society

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# hdfc_obj = HdfcBankaccount(100)
# hdfc_obj.credit(100)
# hdfc_obj.get_balance()
#
# axis_obj = AxisBankaccount(200)
# axis_obj.debit(100)
# axis_obj.get_balance()




rbiObject = AxisBankaccount(200)
rbiObject.debit(250)
rbiObject.get_balance()
rbiObject.credit(100)
rbiObject.get_balance()

rbiObject = HdfcBankaccount(250)
rbiObject.debit(500)
rbiObject.debit(250)
rbiObject.get_balance()
rbiObject.credit(100)
rbiObject.get_balance()


