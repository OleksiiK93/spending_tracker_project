import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

merchant_1 = Merchant("Booking.com")
merchant_repository.save(merchant_1)
# merchant_1.deactivate()
# merchant_repository.update(merchant_1)

merchant_2 = Merchant("Vodafone")
merchant_repository.save(merchant_2)
merchant_3 = Merchant("Scottish Citylink")
merchant_repository.save(merchant_3)

tag_1 = Tag('Holidays')
tag_repository.save(tag_1)
tag_2 = Tag('Bills')
tag_repository.save(tag_2)
tag_3 = Tag('Transport')
tag_repository.save(tag_3)

# transaction_1 = Transaction(merchant_1, tag_1, 55.00)
# transaction_repository.save(transaction_1)
# transaction_2 = Transaction(merchant_2, tag_2, 45)
# transaction_repository.save(transaction_2)
# total = transaction_repository.total()

# merchants = merchant_repository.select_all()
# tags = tag_repository.select_all()
# transactions = transaction_repository.select_all()

# selected_merchant = merchant_repository.select(1)
# selected_tag = tag_repository.select(3)

# merchant_2.name = "Sky"
# result_1 = merchant_repository.update(merchant_2)
# tag_1.name = 'Vacation'
# result_2 = tag_repository.update(tag_1)

transactions = transaction_repository.select_all()

# pdb.set_trace()