# from Bank.axis_bank import AxisBankaccount
# from Bank.hdfc_bank import HdfcBankaccount
# from Bank.test import Test123
# from Utils.generic_utils import GenericUtils
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
rbiObject.debit(150)
rbiObject.get_balance()


# for data in testData:
#     print(data)

print(GenericUtils.get_data('TC002'))