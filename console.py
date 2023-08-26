import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository

merchant_1 = Merchant("Booking.com")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Vodafone")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("Scottish Citylink")
merchant_repository.save(merchant_3)

merchants = merchant_repository.select_all()

selected_merchant = merchant_repository.select(1)

merchant_2.name = "Sky"
merchant_repository.update(merchant_2)

pdb.set_trace()