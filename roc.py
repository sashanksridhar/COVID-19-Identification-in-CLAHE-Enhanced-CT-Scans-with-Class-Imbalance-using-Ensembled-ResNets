import matplotlib.pyplot as plt

tp = [0.9764]
fp = [0.0437]
from sklearn.metrics import auc
auc_rf = auc(fp, tp)
plt.plot(fp,tp,label="(area = {:.3f})".format(auc_rf))
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve')
plt.legend(loc='best')
plt.show()