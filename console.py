import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

merchant_1 = Merchant("Booking.com")
merchant_repository.save(merchant_1)
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

merchants = merchant_repository.select_all()
tags = tag_repository.select_all()

selected_merchant = merchant_repository.select(1)
selected_tag = tag_repository.select(3)

merchant_2.name = "Sky"
result_1 = merchant_repository.update(merchant_2)
tag_1.name = 'Vacation'
result_2 = tag_repository.update(tag_1)

pdb.set_trace()