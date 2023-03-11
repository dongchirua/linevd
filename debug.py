import sastvd.helpers.joern as svdj
import sastvd.ivdetect.helpers as svdh
import sastvd.ivdetect.helpers as ivd
from dgl.dataloading import GraphDataLoader

# svdh.feature_extraction('storage/processed/bigvul/before/88626.c')
# svdh.feature_extraction('storage/processed/bigvul/before/53.c')
# svdh.feature_extraction('storage/processed/bigvul/before/177968.c')
# data = svdh.feature_extraction('storage/processed/bigvul/before/178103.c')
# data = svdh.feature_extraction('storage/processed/bigvul/before/178212.c')
# data = svdh.feature_extraction('storage/processed/bigvul/before/183284.c')
# data = svdh.feature_extraction('storage/processed/bigvul/before/183287.c')
# data = svdh.feature_extraction('storage/processed/bigvul/before/73069.c')
data = svdh.feature_extraction('storage/processed/bigvul/before/72016.c')

# train_ds = ivd.BigVulDatasetIVDetect(partition="train")
# val_ds = ivd.BigVulDatasetIVDetect(partition="val")
# test_ds = ivd.BigVulDatasetIVDetect(partition="test")

# for i in range(len(train_ds)):
#     try:
#         data = train_ds[i]
#         if data is None:
#             print(i)
#     except:
#         print(i)

# train_ds[4382]
# test_ds[501]
# test_ds[7129]


print('end debug')
